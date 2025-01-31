import argparse
import logging
import boto3
from botocore.exceptions import ClientError
import requests

logger = logging.getLogger(__name__)

class S3_session:
    def __init__(self):
        self.bucket_name = "photossocialplanner"
        self.s3_client = boto3.client("s3")
    def Get_presigned_url(self, object_key):
        try:
            url = self.s3_client.generate_presigned_url(
                ClientMethod="get_object",
                Params={
                    "Bucket": self.bucket_name,
                    "Key": object_key
                },
                ExpiresIn=3600
            )
            logger.info("Got presigned URL: %s", url)

        except ClientError:
            logger.exception(
                "Couldn't get a presigned URL for client method '%s'.", "get_object"
            )
            raise
        return url
    def Post_presigned_url(self, object_key):
        try:
            response = self.s3_client.generate_presigned_post(
                Bucket=self.bucket_name,
                Key=object_key,
                ExpiresIn=3600
            )
            logger.info("URL de subida generada con éxito: %s", response["url"])
        except ClientError as e:
            logger.exception(
                "Error al obtener la URL presignada para '%s' en el bucket '%s': %s",
                object_key, self.bucket_name, e.response["Error"]["Message"]
            )
            raise
        return response
    def Upload_file(self, file_name, object_name):
        try:
            self.s3_client.upload_file(file_name, self.bucket_name, object_name)
            logger.info("Archivo subido con éxito")
        except ClientError as e:
            logger.error(f"Error al subir el archivo: {e}")
            raise
        return
    def Download_file(self, object_name, file_name):
        try:
            self.s3_client.download_file(self.bucket_name, object_name, file_name)
            logger.info("Archivo descargado con éxito")
        except ClientError as e:
            logger.error(f"Error al descargar el archivo: {e}")
            raise
        return
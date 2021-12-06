import etcd3
from app import app
import uvicorn

if __name__ == "__main__":
	client = etcd3.client()

	puerto = client.get('puerto')[0].decode('utf-8')
	host = client.get('host')[0].decode('utf-8')
	
	uvicorn.run("app:app", host=host, port=puerto)
HTTP = "http://"
COLON = ":"

# eureka registry config
REGISTRY=False
MY_APPLICATION_NAME = "vision-service"
REG_PORT = "8187"
HEARTBEAT_INTERVAL = 30
STATUS_API = "vision-service/job/status"
DISCOVERY_SERVICE_PORT = "8761"
STORAGE_SERVICE = "storage-service"





DISCOVERY_SERVICE_IP = "127.0.0.1"
INSTANCE_IP = "127.0.0.1"
POSTGRES_IP = "127.0.0.1"
DISCOVERY_SERVICE = HTTP + DISCOVERY_SERVICE_IP + COLON + DISCOVERY_SERVICE_PORT + "/eureka/apps/"

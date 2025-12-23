from cfenv import AppEnv

env = AppEnv()
print(f"name: {env.name}")
print(f"port: {env.port}")
print(f"space: {env.space}")

hdi_db_actionserver = env.get_service(label='hdi_db_actionserver')

if hdi_db_actionserver is not None and bool(hdi_db_actionserver):
    service = hdi_db_actionserver.credentials
    print(service)
else:
    print("Nothing to display")

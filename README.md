# RevApp PoC

## App data

- App code: ./src
- App endpoints:
  - http://revapp.ddns.net/docs
- App health endpoints (Including data for SLI/Os):
  - http://revapp.ddns.net/health
  - http://revapp.ddns.net/metrics
- GitOps manifest to deploy app: ./gitops

## Extra info

- SRE/Monitoring: [SRE](./docs/SRE.md)
- CI/CD and possible strategies [CI-CD](./docs/CI-CD.md)
- Considerations to run/maintain Prod [PROD](./docs/RUNNING_IN_PROD.md)

## TODO:

- GKE should be deployed via Terraform
- Custom logger on APP with FastAPI
- Add DocStrings to all the methods
- Improve the Pydantic modeling
- Move GitOps manifests to another repo
- Not run container as root
- Unit testing
- MongoDB not deployed as standalone, use operator with Sharding/ReplicaSet config.
- Document for SRE SLI/Os observability/maintenance
- Fix CamelCase/snake_case
- Change ISOFormat -> Date MongoDB
- Improve Exception handling
- ... (Open to discuss)


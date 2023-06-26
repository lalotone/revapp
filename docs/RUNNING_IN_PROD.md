# Considerations to run in PROD:

- Some of the tests should not run on pipelines if they are run in PRE.
- Immutable image to have the same version of the images on all envs.
- Caching can be an option to avoid not necessary calls to DB.
- Load-Balancing between multiple cloud providers and regions to increase availability.
- Canary deployments for critical apps to do easy rollback and affect as less people as possible if something went wrong.
- Constant monitoring of all the apps with alerting fine-tuned, also on PRE to detect possible anomalies before going to production.
- HPA and resources of the K8s objects should be adjusted (Requests/Limits).
- If necessary (but **must** be monitored ) implement HPA based on memory. But this should be double-checked to avoid multiple 
replicas that doesn't free the mem.
- Easy way to do rollback to previous version.
- Databases running in HA, Sharding/ReplicaSet for Mongo and Master/Slave(s) Active/Pasive Active/Active for solutions
like MySQL or similar products.
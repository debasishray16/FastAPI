# Setting up a Runner

```text

GitHub Push
   ↓
GitHub Actions
   ↓
Self-hosted Runner (on your VM)
   ↓
Docker build + run (on same VM)

```

## Steps 
1. Create a repository and navigate to settings -> Actions -> Runners
2. Select according to your server specs

```bash

mkdir actions-runner; cd actions-runner

Invoke-WebRequest -Uri https://github.com/actions/runner/releases/download/v2.333.1/actions-runner-win-x64-2.333.1.zip -OutFile actions-runner-win-x64-2.333.1.zip

if((Get-FileHash -Path actions-runner-win-x64-2.333.1.zip -Algorithm SHA256).Hash.ToUpper() -ne 'd0c4fcb91f8f0754d478db5d61db533bba14cad6c4676a9b93c0b7c2a3969aa0'.ToUpper()){ throw 'Computed checksum did not match' }

Add-Type -AssemblyName System.IO.Compression.FileSystem ; [System.IO.Compression.ZipFile]::ExtractToDirectory("$PWD/actions-runner-win-x64-2.333.1.zip", "$PWD")
```

3. Now , you can provide details to the runner

```bash
./config.cmd --url https://github.com/debasishray16/FastAPI --token AUANQLOJXKCRRPEGBY2QLCDJ.....


# Connects to Github
./run.cmd
```

4. Start it as a service to run it 24/7

```bash
sudo ./svc.sh install
sudo ./svc.sh start

# to verify it 
sudo ./svc.sh status


# For auto-start
sudo systemctl enable actions.runner.*
```
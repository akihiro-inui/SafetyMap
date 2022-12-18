# SafetyMap
This application visualizes the safey level of your location.    
This repository involves the backend API and the frontend application.

## Build Status
[![Build Status](https://dev.azure.com/SwiftAI/Safety%20Map/_apis/build/status/akihiro-inui.SafetyMap?branchName=main)](https://dev.azure.com/SwiftAI/Safety%20Map/_build/latest?definitionId=2&branchName=main)

## Dev Deployment
[![Netlify Status](https://api.netlify.com/api/v1/badges/ed110798-4064-4ad9-9635-34b7c31ad4e0/deploy-status)](https://app.netlify.com/sites/safetymap/deploys)

## Folder Structure
```bash
├── docs
├── backend
│   ├── src
│   ├── tests
│   ├── Dockerfile
│   ├── README.md
│   ├── setup.cfg
│   └── setup.py
├── frontend
│   ├── assets
│   ├── components
│   ├── constants
│   ├── hooks
│   ├── navigation
│   ├── screens
│   ├── app.json
│   ├── App.tsx
│   ├── package.json
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   └── eas.json
├── .gitignore
├── azure_pipelines.yml
└── README.md
```

## Frontend
Our frontend application is based on React Native and Expo.  
Find the documentation [here](frontend/README.md)

## Backend
Our backend API is based on Python FastAPI.  
Find the documentation [here](backend/README.md)

## Pipelines
The app is tested and built with the following services.
### Azure DevOps
This pipeline runs the tests for backend API and frontend application  
https://dev.azure.com/SwiftAI/Safety%20Map/_build?definitionId=2&_a=summary

### Expo
This pipelines builds the birary files for iOS and Android for both internal testing and the release version  
https://expo.dev/accounts/swiftai  

### Netlify  
This hosts the test web app  
https://app.netlify.com/sites/safetymap/overview

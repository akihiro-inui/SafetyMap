# SafetyMap
This application visualizes the safety level of your location.    
This repository involves the backend API, data scraper and the frontend application.

## Build Status
[![Build Status](https://dev.azure.com/SwiftAI/Safety%20Map/_apis/build/status/akihiro-inui.SafetyMap?branchName=main)](https://dev.azure.com/SwiftAI/Safety%20Map/_build/latest?definitionId=2&branchName=main)

## Dev Deployment
[![Netlify Status](https://api.netlify.com/api/v1/badges/ed110798-4064-4ad9-9635-34b7c31ad4e0/deploy-status)](https://app.netlify.com/sites/safetymap/deploys)

## Folder Structure
```bash
├── backend
│   ├── src
│   ├── tests
│   ├── Dockerfile
│   ├── setup.py
│   ├── setup.cfg
│   └── README.md
├── web
│   ├── public
│   ├── src
│   │   ├── Components
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── index.css
│   │   ├── index.js
│   │   └── tests
│   ├── package-lock.json
│   ├── package.json
│   └── README.md
├── mobile
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
│   ├── README.md
│   └── eas.json
├── scraper
│   ├── src
│   ├── tests
│   ├── Dockerfile
│   ├── README.md
│   ├── setup.cfg
│   └── setup.py
├── .gitignore
├── azure_pipelines.yml
└── README.md
```

## Web Application
Our web application is built with React.js.  
Find the documentation [here](web/README.md)

## Mobile Application
Our mobile application is based on React Native and Expo.  
Find the documentation [here](mobile/README.md)

## Backend
Our backend API is built with FastAPI.  
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

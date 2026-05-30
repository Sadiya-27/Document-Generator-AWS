# Automated Source Code Documentation Generator

## Overview

The Automated Source Code Documentation Generator is a cloud-based solution that automatically generates technical documentation for Python applications using Sphinx. The project leverages AWS DevOps services to automate the documentation generation workflow, ensuring that documentation remains consistent, up-to-date, and easily accessible.

The system uses Amazon S3 for source code and documentation storage, AWS CodePipeline for workflow orchestration, AWS CodeBuild for build automation, and Sphinx for generating HTML documentation from Python source code.

---

## Features

* Automated documentation generation using Sphinx
* Continuous Integration workflow using AWS CodePipeline
* Automated build process using AWS CodeBuild
* Storage of source code and generated documentation in Amazon S3
* Infrastructure deployment using AWS CloudFormation
* CloudWatch monitoring and logging
* Linux-based build environment
* Scalable and serverless architecture

---

## Architecture
<img width="1536" height="1024" alt="architecture" src="https://github.com/user-attachments/assets/f08ff66f-71f0-4521-b5cd-01beeea724bb" />


```text
Developer
    │
    ▼
Amazon S3 (Source Code)
    │
    ▼
AWS CodePipeline
    │
    ▼
AWS CodeBuild
    │
    ├── Install Dependencies
    ├── Run Sphinx
    └── Generate HTML Documentation
    │
    ▼
Amazon S3 (Generated Documentation)
    │
    ▼
Users / Developers
```

---

## Workflow

1. Upload Python source code to the S3 source bucket.
2. AWS CodePipeline automatically detects changes.
3. CodePipeline triggers AWS CodeBuild.
4. CodeBuild installs required dependencies.
5. Sphinx scans the source code and generates documentation.
6. HTML documentation is created.
7. Generated documentation is uploaded to Amazon S3.
8. Documentation becomes available for users and developers.

---

## AWS Services Used

* Amazon S3
* AWS CodePipeline
* AWS CodeBuild
* AWS CloudFormation
* AWS IAM
* Amazon CloudWatch

---

## Technologies Used

* Python
* Sphinx
* AWS DevOps Services
* Linux
* HTML
* reStructuredText (RST)

---

## Project Structure

```text
project/
│
├── source/
│   ├── app.py
│   ├── utils.py
│   ├── models.py
│
├── docs/
│   ├── conf.py
│   ├── index.rst
│   ├── modules.rst
│
├── buildspec.yml
├── template.yaml
└── README.md
```

---

## Sphinx Documentation Generation

Generate API documentation:

```bash
sphinx-apidoc -o docs source/
```

Build HTML documentation:

```bash
sphinx-build -b html docs docs/_build/html
```

---

## Buildspec Configuration

```yaml
version: 0.2

phases:
  install:
    commands:
      - pip install sphinx

  build:
    commands:
      - sphinx-apidoc -o docs source/
      - sphinx-build -b html docs docs/_build/html

artifacts:
  files:
    - '**/*'
```

---

## Security

The project follows AWS security best practices:

* IAM Least Privilege Access
* Controlled S3 Bucket Permissions
* CloudFormation-managed resources
* CloudWatch monitoring and logging
* Secure artifact handling within AWS services

---

## Monitoring

Amazon CloudWatch is used to monitor:

* Pipeline executions
* Build status
* Documentation generation logs
* Error tracking and debugging

---

## Benefits

* Reduces manual documentation effort
* Improves documentation consistency
* Automates documentation generation workflow
* Supports continuous integration practices
* Easy deployment and scalability
* Centralized storage and accessibility

---

## Future Enhancements

* Support for multiple programming languages
* Automatic versioning of documentation
* Documentation quality analysis
* Integration with additional CI/CD tools
* Automated deployment to static documentation websites

---

## Conclusion

This project demonstrates the implementation of an automated documentation generation platform using Python, Sphinx, AWS CodePipeline, AWS CodeBuild, and Amazon S3. By automating the documentation process, developers can maintain accurate and consistent technical documentation while reducing manual effort and improving development efficiency.


# Async AWS Cognito JWT validation in Python

This is a work in progress - not tested - no Cognito User Pool access.

To retrieve the JWT Token, either a login operation from the Cognito Hosted UI can be used, or the AWS provided [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html)
or [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html) API calls can be used.

Now to verify the incoming token with Cognito following this AWS doc [Verifying a JSON Web Token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html)
a python file [aws-cognito-jwt.py](./aws-cognito-jwt.py) was created using [cognitojwt async module](https://pypi.org/project/cognitojwt/).

Please note, if the application is deployed inside a private vpc without internet gateway, the application will not be able to download the JWKS file.
In this case set the `AWS_COGNITO_JWKS_PATH` environment variable referencing the absolute or relative path of the jwks.json file.



## Requirements

Python >= 3.6 for cognitojwt

```bash
pip install cognitojwt[async] --user
```

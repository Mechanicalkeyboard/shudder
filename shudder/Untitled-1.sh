#!/bin/bash
set -v -x
Environment=dev
Host=cxengagelabs
Service=edge
Region=us-east-1
echo Environment is $Environment
echo Host name is $Host
echo Service is $Service
echo Region is $Region
echo "IF GATEWAY INSTALL THE PEM FILES"
if [[ "$Service" = *"gateway"* ]]; then 
echo "INSTALLING PEM FILE"
curl --silent https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem > /tmp/CA.pem
sudo mv /tmp/CA.pem /lo/conf/CA.pem
sudo aws iot attach-principal-policy --policy-name internal_gateway --principal $(sudo aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile /lo/conf/cert.pem --public-key-outfile /lo/conf/publicKey.pem --private-key-outfile /lo/conf/privateKey.pem --region $Region | jq -r .certificateArn) --region $Region
fi
echo "INSTALLING PROPERTIES FILE"
sudo wget --quiet http://$Host-clusters.s3.amazonaws.com/$Service-$Region-$Environment.properties -O /lo/conf/$Service-$Region-$Environment.properties
sudo wget --quiet http://$Host-clusters.s3.amazonaws.com/$Service-$Region-$Environment.cluster -O /etc/init.d/cluster
bash /etc/init.d/cluster
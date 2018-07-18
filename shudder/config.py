# Copyright 2014 Scopely, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration for shudder"""
import os
import toml

#old
# CONFIG_FILE = os.environ.get('CONFIG_FILE', "shudder.toml")
# CONFIG = {}
# with open(CONFIG_FILE, 'r') as f:
#     CONFIG = toml.loads(f.read())
# print(CONFIG)

service=os.environ['service']
region=os.environ['region']
environment=os.environ['environment']
accountArn=os.environ['accountArn']


CONFIG = {'sqs_prefix': service + '-shutdown', 'region': region, 'sns_topic':"arn:aws:sns:"+accountArn+':'+region+'-'+environment+'-'+service+'-shutdown','commands':'[["python","shudder/serviceShutdown.py"]]'}
print(CONFIG)

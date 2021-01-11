# Ansible Collection - kemopq.hello_world
This collection is an example. It's made to illustrate typical construction and usage of ansible collections.
It can also be used as a base for other more advances collections. 
The integration testing with molecule is included and also described on testing README. 
The collection consists of two roles and two plugins (filter and module). 
The descriptions of roles and plugins are in README files on role's and plugin's folder.

### Requirements
Install python3, pip3 and ansible:
```
sudo apt update
sudo apt install python3 python3-pip
sudo pip3 install ansible
```

### Installing collection  
Install this collection locally:
```
ansible-galaxy collection install kemopq.hello_world -p ./collections
```
_./collections_ folder should be included to _collections_path_ parameter in ansible configuration file. See:
https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations
```
[defaults]
collections_path = ./collection
host_key_checking = False
```
Additional parameter host_key_checking is added, so ssh is done without key checking.

### Using collection  
Roles and plugins can be used on your ansible playbook. It can be referenced by its fully qualified collection name (FQCN):
```
---
- name: Your awesome playbook
  hosts: all
  gather_facts: 'no'

  tasks:
    - name: "Include hello_world role"
      include_role:
        name: "kemopq.hello_world.hello_world_role"

    - name: "Include print_facts role"
      include_role:
        name: "kemopq.hello_world.print_facts_role"

    - name: "Add sign to file /tmp/testfile.txt"
      kemopq.hello_world.signfile:
        name: Bruce Willis
        path: "/tmp/testfile.txt"

    - name: Print string to_upper
      vars:
        in_string: "Today is holiday"
      debug:
        msg: "{{ in_string | kemopq.hello_world.hw_to_upper }}"
```
or using _collections_ keyword to define collection and then using simple names of roles (plugins still need FQCN):
```
---
- name: Your awesome playbook
  hosts: all
  gather_facts: 'no'

  collections:
    - kemopq.hello_world

  tasks:
    - name: "Include hello_world role"
      include_role:
        name: "hello_world_role"

    - name: "Include print_facts role"
      include_role:
        name: "print_facts_role"

    - name: "Add sign to file /tmp/testfile.txt"
      signfile:
        name: Bruce Willis
        path: "/tmp/testfile.txt"

    - name: Print string to_upper
      vars:
        in_string: "Today is holiday"
      debug:
        msg: "{{ in_string | kemopq.hello_world.hw_to_upper }}"
```
More info can be read on:
https://docs.ansible.com/ansible/latest/user_guide/collections_using.html

### Runing your playbook on localhost
Enable passwordless ssh to localhost:
```
cd .ssh
ssh-keygen
cat id_rsa.pub >> authorized_keys
```
Run ansible playbook:
```
ansible-playbook -i localhost, your_playbook.yml
```

### Testing collection
Testing of the collection is done by _Molecule_ testing tool with Docker driver. The roles and module is tested on two hosts (Centos8, Ubuntu2008). Docker images prepared by @geerlingguy are used.  
Running test:  
Go to the collection main folder and run 
```
molecule test
```
More about testing is described in README on _molecule_ folder.

### Make your own collection
Best way is to copy this hello_world collection to your _ansible_collections/\<your_namespace>/\<your_collection>_ and integrate your roles and/or plugins.
The other way is to use ansible-galaxy tool to create basic folder structure of your collection:  
Go to the ansible_collections folder and run:
```
ansible-galaxy collection init <your_namespace>.<your_collection>
```
More info on:
https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#developing-collections

### Publish your collection
Prepare galaxy metadata file _galaxy.yml_ . Then build your collection.  
Go to collection main folder and run (use --force in case of rebuilding):  
```
ansible-galaxy collection build
```
_\<your_namespace>-\<your_collection>-\<version>.tar.gz_   file is generated.
Login to https://galaxy.ansible.com , collect token (show API key) and run:
```
ansible-galaxy collection publish ./<your_namespace>-<your_collection>-<version>.tar.gz --token=<your_token>
```

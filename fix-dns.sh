#!/bin/bash
##set namespace
NAMESPACE="namespace-01"
kubectl config use-context $NAMESPACE
##remove old accepted certificates
kubectl exec -it jumpbox -- rm -f /root/.ssh/known_hosts
##get worker VMs
VM=$(kubectl get vm)
for VMNAME in $VM
do
  #if it is a worker vm
  if [[ "$VMNAME" == *'tkg'*'worker'* ]]; then
     #set IP
     VMIP=$(kubectl -n $NAMESPACE get virtualmachine/$VMNAME -o jsonpath='{.status.vmIp}')
     #log in to accept new ssh key
     kubectl exec -it jumpbox -- /usr/bin/ssh -o StrictHostKeyChecking=accept-new vmware-system-user@$VMIP 'pwd'
     #add harbor.dell.local to local resolver
     kubectl exec -it jumpbox  /usr/bin/ssh vmware-system-user@$VMIP "sudo sed -i '$ a 192.168.1.229 harbor.dell.local' /etc/hosts"
  fi
done

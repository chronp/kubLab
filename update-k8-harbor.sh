#!/bin/bash
##set namespace
NAMESPACE="namespace-01"
kubectl config use-context $NAMESPACE

#copy the root ca to the jumphost
kubectl cp harbor_registry.crt $NAMESPACE/jumpbox:/root/harbor.crt

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
     #copy the root ca to worker
     kubectl exec -it jumpbox  /usr/bin/scp /root/harbor.crt vmware-system-user@$VMIP:/home/vmware-system-user/harbor.crt
     #copy ca cert to cert store
     kubectl exec -it jumpbox  /usr/bin/ssh vmware-system-user@$VMIP 'sudo bash -c "cat /home/vmware-system-user/harbor.crt >> /etc/pki/tls/certs/ca-bundle.crt"'
     #restart docker
     kubectl exec -it jumpbox  /usr/bin/ssh vmware-system-user@$VMIP 'sudo systemctl restart docker.service'
  fi
done

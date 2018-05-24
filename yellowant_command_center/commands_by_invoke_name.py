"""Mapping for command invoke name to logic"""
from .commands import create_item, get_list, get_item, update_item, delete_item ,list_all_vms,create_vm,delete_vm,\
    stop_vm,restart_vm,start_vm,create_resource_group,delete_resource_group,list_all_vms_in_rg,attach_disk,create_disk,detach_disk


commands_by_invoke_name = {
    "createitem": create_item,
    "getlist": get_list,
    "getitem": get_item,
    "updateitem": update_item,
    "deleteitem": delete_item,
    "createvm": create_vm,
    "deletevm": delete_vm,
    "stopvm": stop_vm,
    "restartvm" : restart_vm,
    "startvm" : start_vm,
    "create_resgrp" : create_resource_group,
    "delete_resgrp" : delete_resource_group,
    "listallvms" : list_all_vms,
    "listallvmsinrg" :list_all_vms_in_rg,
    "attachdisk": attach_disk,
    "createdisk" : create_disk,
    "detachdisk" : detach_disk

}
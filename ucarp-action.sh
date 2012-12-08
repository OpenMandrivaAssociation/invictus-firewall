#!/bin/sh

INTERFACE=$1
ACTION=$2
[ -n "$INTERFACE" ] || exit
[ "$ACTION" = add -o "$ACTION" = del ] || exit

UCARP_D=/etc/ucarp.d
CONFIG=$UCARP_D/$INTERFACE
[ -f $CONFIG ] || exit
source $CONFIG

# compute NETMASK
eval `/bin/ipcalc --netmask $VIRTIP`
# compute PREFIX
eval `/bin/ipcalc --prefix $VIRTIP $NETMASK`

/sbin/ip addr $ACTION $VIRTIP/$PREFIX dev "$INTERFACE"
if [ "$ACTION" = add -a -w /proc/sys/net/ipv4/netfilter/ct_sync/state ]; then
    echo "2" > /proc/sys/net/ipv4/netfilter/ct_sync/state
fi

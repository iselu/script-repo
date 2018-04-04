#/etc/rsyslog.d/login.conf
#local3.debug   /var/log/message
remoteip=$(who am i | awk '{print $5}' | sed "s/[()]//g" )
[ -x /usr/bin/id ] || return
curr_id=$(/usr/bin/id -u)
if [ $curr_id -eq 0 ]
then
        prompt='#'
else
        prompt='$'
fi
export PROMPT_COMMAND='RETRN_VAL=$?;logger -p local4.notice "remoteip:[$remoteip] pid:[$$] [$(whoami)@$(pwd)]$prompt $(history 1 |sed "s/^[ ]*[0-9]\+[ ]*//g") [$RETRN_VAL]"'
export PS1="\n[\e[0;35m\t \e[0;31m\u@\H\e[m:\e[0;35m\w\e[m]\n\\$ "


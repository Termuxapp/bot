3
�7|[�B  �               @   s�  e d � ddlZddlZddlmZ ddlmZ ddlmZ ddlZddlZddlZddl	Z	ddl
Z
ddlZddlZddlZddlZddlZejZejZeje�Zdje�Ze	jje�Zej� Zejejd��Zed d	 Zed d
 Zejdddd�Z dje�Z!dje�Z"e j#dje���r4e$e j#dje���Z%neZ%ej&dgd�dd� �Z'ej&dgd�dd� �Z(ej&dgd�dd� �Z)ej&dgd�dd� �Z*ej&dgd�dd � �Z+ej&d!gd�d"d#� �Z,ej&d$gd�d%d$� �Z-ej&d&gd�d'd(� �Z.ej&d)d*gd�d+d)� �Z/ej&d,gd�d-d,� �Z0ej&d.gd�d/d0� �Z1ej&d1gd�d2d1� �Z2ej&d3gd�d4d1� �Z2ej&d5gd�d6d7� �Z3ej&d8d9d:d;d<d=d>gd?�d@dA� �Z4ej&dBdC� dD�dEdF� �Z5ej6dG� dS )Ha�	  
                                ::""!!ffffff!!""::
                          ::!!zznnzzzzzzzzzzzzzzzzzz!!::
                        !!nnzzzzzzzzzzzzzzxxzzzzzzzzzznn""
                    ::nnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz::
                  ;;nnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz;;
                ;;nnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz;;
              ::nnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznn::
              zzzzzzzzzzzzzzzzzzzz--@MR_MUSA--zzzzzzzzzzzzzzzzzzzzzzz
            !!zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznn""
            nnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzzzzzzzzzzzzzzz
          !!zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnff;;  !!zzzzzzzzzznn;;
          zzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnzz""        ffzzzzzzzzzznnff
        ::nnzzzzzzzzzzzzzzzzzzzzzzzznnnnff::    ::::    nnzzzzzzzzzzzznn
        ;;nnzzzzzzzzzzzzzzzzzznnnnzz""        ;;::      nnzzzzzzzzzzzznn::
        !!nnzzzzzzzzzzzznnnnnn!!::        ::;;::      ;;nnzzzzzzzzzzzznn;;
        !!nnzzzzzzzznnnnff;;            ;;;;          !!nnzzzzzzzzzzzznn""
        ffnnzzzzzzzznn::            ::;;;;           ffnnnzzzzzzzzzznnnn!!
        !!nnzzzznnzznnzz""::      ;;;;;;             zznznzzzzzzzzzzzznn!!
        ""nnzzzzzzzzzznnnnnnzz"";;;;;;              ::nnzzzzzzzzzzzzzznn;;
        ;;nnnnzzzznnzzzznnnnnnzz::;;                ;;nnzzzzzzzzzzzznnee::
          nnnnzzzznnzzzzzzzznnnn;;;;""::            ffnnnnnnzzzznnnnnnnn
          zznnnnnnnnnnnnnnnnnnnn"";;""""""          nnnnnnnnnnnnnnnnnnzz
          ""nnnnnnnnnnnnnnnnnnnnzz;;;;zzeeff        eennnnnnnnnnnnnnee;;
            nnnnnnnnnnnnnnnnnnnnnn""nnnnnnnnnn::  ;;nnzznnnnnnnnnnnnnn
            ""eennnnnnnnnnnnnnnnzznnnnnnnnnnnnee!!zznnnnnnnnnnnnnnee;;
              zznnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnzz
              ::nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
                ::eennnnnnnnnnnnnnnnnnnnnnazinnnnnnnnnnnnnnnnee::
                  ::nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn::
                    ::nneennnnnnnnnnnnnnnnnnnnnnnnnnnnnneezz
                        ""eeeennnnnnnnnnnnnnnnnnnnnneenn;;
                            ""zzeeeeeeeeeeeeeeeeeezz;;
                                  ;;""!!!!!!""::

                                                                                                                                                                                
                                    @mr_musa
�    N)�types)�util)�randintz%https://api.telegram.org/bot{}/getMe?zutf-8�result�id�usernameZ	localhosti�  )�hostZport�dbzbanned:users:{}zpmresan:users:{}z
logchat:{}Zsetstart)Zcommandsc             C   sh   yN| j jtkrL| jjdd�}tjdjtt	��|� t
j| j jdj|�dd� W n   td� Y nX d S )Nz
/setstart � z
welcome:{}z*Welcome TexT Changed To :*
{}�Markdown)�
parse_mode�Error)�chatr   �logchat�text�replace�R�set�format�str�botid�bot�send_message�print)�mr   � r   �pm.py�shstartJ   s    r   Zsetwaitc             C   s~   yN| j jtkrL| jjdd�}tjdjtt	��|� t
j| j jdj|�dd� W n* tk
rx } zt|� W Y d d }~X nX d S )Nz	/setwait r
   zwait:{}z*Wait TexT Changed To :*
{}r   )r   )r   r   r   r   r   r   r   r   r   r   r   r   �	Exceptionr   )r   r   �er   r   r   �
show_alertS   s    r    Zsetfloodc             C   s~   yN| j jtkrL| jjdd�}tjdjt�t	|�� t
j| j jdj|�dd� W n* tk
rx } zt|� W Y d d }~X nX d S )Nz
/setflood r
   z
maxmsgs:{}z*Flood Messages Changed To {}*r   )r   )r   r   r   r   r   r   r   r   �botuser�intr   r   r   r   )r   r   r   r   r   r   �sflood\   s    r#   Zsetfloodtimec             C   s~   yN| j jtkrL| jjdd�}tjdjt�t	|�� t
j| j jdj|�dd� W n* tk
rx } zt|� W Y d d }~X nX d S )Nz/setfloodtime r
   zmaxflood:{}z*Flood Time Changed To {}*r   )r   )r   r   r   r   r   r   r   r   r!   r"   r   r   r   r   )r   r   r   r   r   r   �sfte   s    r$   Z	enableadsc             C   sb   y2| j jtkr0tjdjt�d� tj| j jd� W n* t	k
r\ } zt
|� W Y d d }~X nX d S )Nzads:{}Tuz   تبلیغات کانال ترموکس در ربات شما فعال شد
ممنون که مارو حمایت میکنید)r   r   r   r   r   r   r!   r   r   r   r   )r   r   r   r   r   �sadsn   s    r%   Z
disableadsc             C   s`   y0| j jtkr.tjdjt�� tj| j jd� W n* t	k
rZ } zt
|� W Y d d }~X nX d S )Nzads:{}u<   تبلیغات و حمایت شما از ما قطع شد :()r   r   r   r   �deleter   r!   r   r   r   r   )r   r   r   r   r   �sadsdv   s    r'   �setlogc             C   st   yD| j jtkrBtjdjt�| jj� tj	| jjdj| jj�dd� W n* t
k
rn } zt|� W Y d d }~X nX d S )Nz
logchat:{}z*New Log Chat Set*
`ID` : _{}_r   )r   )�	from_userr   �sudor   r   r   r!   r   r   r   r   r   )r   r   r   r   r   r(   ~   s    "Zdellogc             C   sf   y6| j jtkr4tjdjt�t� tj| j	jddd� W n* t
k
r` } zt|� W Y d d }~X nX d S )Nz
logchat:{}z*Old Log Chat Deleted*r   )r   )r)   r   r*   r   r   r   r!   r   r   r   r   r   )r   r   r   r   r   �remlog�   s    r+   �start�helpc             C   s�   y�| j jtkr$d}tjt|dd� n�| j jtks�tj� }|jtjddd�� t	j
djtt���rvt	j
djtt���}nd}t	j
d	jt��r�tj| j j|d|d
� ntj| j j|dd� W n* tk
r� } zt|� W Y d d }~X nX d S )Nuj  سلام رئیس 👋
دستورات از این قراره:

/setstart <text>
تنظیم متن شروع با قابلیت مارکداون
/setwait <text>
تنظیم متن ارسالی به کاربر بعد از پیام های وی با قابلیت مارکدون
/ban <on reply/id>
بن کردن یک نفر از پیام رسان
/unban <on reply/id>
آن بن کردن یک نفر از پیام رسان
/users
تعداد کاربران
/bans
تعداد افراد بن شده
/showstart
نمایش متن استارت فعلی
/showwait
دریافت متن انتظار فعلی
/setlog <in group or private>
تنظیم یک گروه به عنوان گروه ادمین
/dellog
حذف گروه ادمین
/sendtoall <text>
ارسال یک متن به تمامی کاربران
/fwdtoall <on reply>
فوروارد یک پیام به تمامی اعضا
/setflood <num>
تنظیم تعداد پیام های ارسالی برای تشخیص اسپم (پیشفرض : ۵ در ۴ ثانیه)
/setfloodtime <num>
تنظیم زمان محدودیت ارسال پیام(پیشفرض : ۴)
/msg <id> <text>
فرستادن یک پیام به یک شخص از طریق آیدی
/enableads
حمایت از ما با تبلیغ سورس ربات :)
/disableads
قطع حمایت از ما :(

نکته :‌برای جواب دادن به اشخاص روی پیام آنها ریپلای کنید
نکته : پیشنهاد میشه تنظیمات فلود رو دستکاری نکنید 

با آروزی خوشحالی برای شما
منتظر سورپرایز ها در ورژن بعدی باشید
[Termuxapp](https://telegram.me/Termuxapp)r   )r   u   کانال ترموکس ماzhttps://telegram.me/Termuxapp)Zurlz
welcome:{}z9*Welcome Dude ,*
_I'll Forward Your Message To Bot Owner_zads:{})r   Zreply_markup)r   r   r   r   r   r   ZInlineKeyboardMarkup�addZInlineKeyboardButtonr   �getr   r   r   r!   r   r   )r   r   Zmarkup�tex3r   r   r   r   r,   �   s    �sendallc          
   C   s`   | j jtkr\| jjdd�}tjt�}x6|D ].}ytj	||� W q*   tj
t|� Y q*X q*W d S )Nz	/sendall r
   )r   r   r   r   r   r   �smembers�mhashr   r   �srem)r   r   �idsr   r   r   r   r1   �   s    

Zfwdtoallc             C   sf   | j jtkrb| jrb| jj}tjt�}x<|D ]4}ytj	|| j j|� W q*   tj
t|� Y q*X q*W d S )N)r   r   r   �reply_to_message�
message_idr   r2   r3   r   �forward_messager4   )r   Zmidr5   r   r   r   r   �fwdall�   s    

r9   �unbanc             C   s�   | j s�| jjtkr�y^| j rD| j jrn| j j}tjt|� tj	td� n*| j
jdd�}tjtt|�� tj	td� W n* tk
r� } zt|� W Y d d }~X nX d S )N�Unbannedz/unban r
   )r6   r   r   r   �forward_fromr   r4   �bhashr   r   r   r   r"   r   r   )r   �userr   r   r   r   r   r:   �   s    Zbanc             C   s�   | j s�| jjtkr�y^| j rD| j jrn| j j}tjt|� tj	td� n*| j
jdd�}tjtt|�� tj	td� W n* tk
r� } zt|� W Y d d }~X nX d S )Nr;   z/ban r
   ZBanned)r6   r   r   r   r<   r   r4   r=   r   r   r   r   �saddr"   r   r   )r   r>   r   r   r   r   r   r:   �   s    �msgc             C   sz   | j sv| jjtkrvyJ| jj� d }| jj� d }t|�}tjtdj	|�dd� tj||� W n   tjtd� Y nX d S )N�   �   zMessage Sent To *{}*r   )r   z'Message Not Sent
iThink User Blocked Me)
r6   r   r   r   r   �splitr"   r   r   r   )r   r   r   Zreceiverr   r   r   �smsg�   s    rD   �video�photo�sticker�document�audio�voicer   )Zcontent_typesc             C   s�  �y�| j �rJ| jjtk�rz| jrl| j }| jjj}| j dkr>d S | j dkrLd S tj||� tj| jjd� �qF| j�sF| j dkr�tj	t
�}djt|��}tjt|� n�| j dkr�tj	t�}djt|��}tjt|� n�| j dk�r&tjd	jtt����rtjd	jtt���}nd
}tj| jj|dd� nP| j dk�rFtjdjtt����r^tjdjtt���}nd}tj| jj|dd� �q�| jjtk�s�djt| jj�}d}	d}
tj|��r�ttj|��}	tj|�}
n"tjdjt���r�tjdjt��}
tj||
t|	�d � | jjdk�r�tjt
| jj��r2tj| jjd� �q�tjt
| jj��s�| j dk �s`| j dk �r�tjt| jj��s�tjdjtt����r�tjdjtt���}nd}tjt| jj� tjt| jj| j� tj| jj|dd� njtjt| jj��r�tjdjtt����rtjdjtt���}nd}tjt| jj| j� tj| jj|dd� �nj| jjtk�r2| j�r�| jjj}| j�r�| jd j}tj||� n�| j�r�| jj}tj||� nv| j�r�| jj}tj ||� nX| j!�r�| j!j}tj"||� n:| j#�r| j#j}tj$||� n| j%�r | j%j}tj&||� tj| jjd� n�| jjtk�s�tjt| jj| j� tjdjtt����r�tjdjtt���}nd}tjtdj| jj'| jj(�� tj| jj|dd� W n, t)k
�r� } zt*|� W Y d d }~X nX d S )Nz/banz/unbanzMessage Sentz/banszBanned Users : {}z/userszBot Users : {}z
/showstartz
welcome:{}z9*Welcome Dude ,*
_I'll Forward Your Message To Bot Owner_r   )r   z	/showwaitzwait:{}z*Message Sent*zanti_flood:{}:{}r   �   zmaxflood:{}rA   ZprivatezYou're Bannedz/startz/helpzMessage Sent by {} - @{})+r   r   r   r   r6   r<   r   r   r   Zscardr=   r   r   r3   r/   r   r!   r)   r"   ZttlZsetex�typeZ	sismemberr?   r8   r7   rF   �file_idZ
send_photorE   Z
send_videorG   Zsend_stickerrH   Zsend_documentrI   Z
send_audiorJ   Z
send_voice�
first_namer   r   r   )r   r   r>   �resZtexZres2Ztex2r0   �_hash�msgsZmax_timerM   r   r   r   r   �mfwdr�   s�    







rR   c             C   s   dS )NTr   )�messager   r   r   �<lambda>F  s    rT   )�funcc             C   s�   y�dj t| jj�}d}tj|�r.ttj|��}d}tjdj t��rRtjdj t��}||kr�tjt| jj� dj | jj	| jj
�}d}tjt|� tj| jj|� W n* tk
r� } zt|� W Y d d }~X nX d S )Nzanti_flood:{}:{}r   rK   z
maxmsgs:{}zUser {} - @{} is Floodingz$Flood Is Not Allowed !
You're Banned)r   r!   r)   r   r   r/   r"   r?   r=   rN   r   r   r   r   r   r   )r   rP   rQ   Zmax_msgsr   Ztext2r   r   r   r   �fwdrF  s     
rV   T)7r   ZtelebotZrandomr   r   r   ZjsonZredisZloggingZurllibZtime�
subprocessZrequests�os�config�tokenr*   ZTeleBotr   r   r	   ZrequestZurlopenrO   �readZres_body�loads�decodeZparsed_jsonr   r!   ZStrictRedisr   r=   r3   r/   r"   r   Zmessage_handlerr   r    r#   r$   r%   r'   r(   r+   r,   r1   r9   r:   rD   rR   rV   Zpollingr   r   r   r   �<module>   s`   %



				
"d
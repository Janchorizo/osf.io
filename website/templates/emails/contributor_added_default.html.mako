<%inherit file="notify_base.mako" />

<%def name="content()">
<tr>
  <td style="border-collapse: collapse;">
    <%!
        from website import settings
    %>
    Hello ${user.fullname},<br>
    <br>
    ${referrer_name + ' has added you' if referrer_name else 'You have been added'} as a contributor to the project "${node.title}" on the PROVIDEDH Collaborative Platform: ${node.absolute_url}<br>
    <br>
    You will ${'not receive ' if all_global_subscriptions_none else 'be automatically subscribed to '} notification emails for this project. To change your email notification preferences, visit your project or your user settings: ${settings.DOMAIN + "settings/notifications/"}<br>
    <br>
    If you are erroneously being associated with "${node.title}," then you may visit the project's "Contributors" page and remove yourself as a contributor.<br>
    <br>
    Sincerely,<br>
    <br>
    The PROVIDEDH Robot<br>
    <br>
    Want more information? Visit https://providedh.ehum.psnc.pl/ to learn about the PROVIDEDH Collaborative Platform, or https://providedh.eu/ for information about the PROVIDEDH CHIST-ERA Project.<br>
    <br>
    Questions? Email ${osf_contact_email}<br>

</tr>
</%def>

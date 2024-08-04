Virtual Phone Numbers
=================
Definiton: A *Virtual Phone Number* is a telephone number that is not tied to any physical location or device.

Problem: Many online accounts, including banks, require SMS/call verification and do not offer a superior method. Typically, the Carrier Phone Number that comes with a cellphone plan is used for this verification. This method, from these providers, is a major failure in our age of technology for 2 reasons:

    - It is incredibly insecure - SIM-swapping is not uncommon.
    - It is an incredibly fragile verification method. If a phone is lost/stolen/damaged beyond usage or if you happen to be using a different SIM card (Eg. traveling), you can be without access to your most critical online accounts.

Solution: Use a few *Virtual Phone Number* providers.

.. warning::

   This approach is debated as a reliable method and may not be the intended use by the *Virtual Phone Number* providers. From experience, if one of the virtual numbers is accepted by the online account, it has NOT been rejected later. Further, it is defended here that using *Virtual Phone Numbers* is a much more robust and secure approach than relying on a Carrier Number, since *Virtual Phone Number* providers can be used on any new phone with any method of internet access (wifi or data from any SIM/cell provider).

Implementation: One will be configured now and others can be added :doc:`later <virtual phone numbers continued>`, when needed (often a total of 3 or 4 is sufficient).

Resulting workflow: Typical login steps
   
   - Enter an account password from the :doc:`password manager` Tutorial
   - Enter a *2FA* code from the :doc:`2 factor authentication` Tutorial
      
      - If this option is not availalable, an SMS will be recieved and used, from this Tutorial.

.. note::

   Calls/messages to 911 (emergency) should use the local SIM, which is ideal.


These options were chosen for Security, Reliability and Availabilty.

.. _virtual-phone-numbers-esim-provider:

Aquire an eSIM - if possible
---------

There will be exceptions, where *Virtual Phone Numbers* will not be accepted. A minimal plan for SMS and calls should be chosen from an eSIM provider (smartphone and region must be compatible). A Web Search like ``eSIM MVNO your_region budget`` can help.

   - For account verification, use this as the very last resort. Wherever possible, use *Virtual Phone Numbers*.
   - If eSIM is not an option for you, know that any account associated with your physical SIM/phone provider is less secure and losing this phone/SIM card will potentially prevent your access to these associated accounts.

.. note::

   Regardless of eSIM usage, continue below.

.. _virtual-phone-numbers-choose-primary-provider:

Choose a Virtual Phone Number Provider
---------

Choose one of these providers for the Primary Virtual Phone Number

   - |logo_googlevoice| Google Voice
   
      - Google wants the account created within the USA
      - Does not support email-to-SMS
      - Most secure 
            
         - Supports :doc:`2 factor authentication`
      - :ref:`Get Started <virtual-phone-numbers-googlevoice>`

   - |logo_textnow| TextNow

      - $8 USD per month on Android and similar on iOS
      - Problematic sending pictures via Android
      - Not supported by WhatsApp
      - Does not support email-to-SMS
      - Advertisements
      - :ref:`Get Started <virtual-phone-numbers-textnow>`

.. |logo_googlevoice| image:: images/virtual_phone_numbers/logo_googlevoice.png
   :width: 8%

.. |logo_textnow| image:: images/virtual_phone_numbers/logo_textnow.png
   :width: 8%



.. _virtual-phone-numbers-googlevoice:

|logo_googlevoice_bg| Google Voice
-------------------

.. |logo_googlevoice_bg| image:: images/virtual_phone_numbers/logo_googlevoice.png
   :width: 15%

This service is used to send/receive messages and calls.

.. _virtual-phone-numbers-googlevoice-install:

|logo_googlevoice| Install
^^^^^^^^^^^^^^^^^^^^^^

.. |logo_googlevoice| image:: images/virtual_phone_numbers/logo_googlevoice.png
   :width: 8%
   
Install on your smartphone.

.. note::

   External link (choose Personal Use): https://voice.google.com/about

.. _virtual-phone-numbers-googlevoice-account:

|logo_googlevoice| Account
^^^^^^^^^^^^^^^^^^^^^^

*Google Voice* requires that the account be created from within the U.S.A.

.. warning::

   If on a smartphone and outside of the U.S.A., setting up the *Google Voice* account over a VPN may fail and another, new Google Account may need to be used.

On a computer:
   
   - Within *Bitwarden*, create an account entry for the new Google Account.
      
      - Suggestion: the email address could be similar to your :ref:`password-manager-core-email-account`, by appending ``_gv``, like this ``example_gv@gmail.com``
         
      - Alternatively, the core email account could be used.

   - In the browser, create/log into the Google Voice account, with copy/paste from *BitWarden*.
      
      - On the *Google Voice* webpage, choose a new *Google Voice* phone number to use:
      
         - Suggestion: choose an area code and region where you have not lived (this helps to identify spam). This will be a temporary phone number. Follow the next steps.
      
      - From any U.S.A. phone provider, purchase the cheapest pre-paid cellphone plan for a month, then port the number to Google Voice for a 1-time fee of $20.  This ensures that your phone number will not change in Google Voice. This is critial for SMS-based account verification.

.. note:: Port a phone number to Google Voice:
   
   - External link: https://support.google.com/voice/answer/1065667?hl=en

.. warning::

   Do not rely upon the free number provided. Google will reuse the phone number for another account after a period of inactivity. A ported number will resolve this. It is a 1-time fee and will dedicate this number to this account.


In this *BitWarden* account entry's Notes section, add a line saying something like: ``VN GoogleVoice your_number``

.. _virtual-phone-numbers-googlevoice-configure:

|logo_googlevoice| Configure
^^^^^^^^^^^^^^^^^^^^^^

On your smartphone, open the Google Voice app and sign in. Verify that the intended Google Account is selected and then configure settings:
   
   - Add a linked phone number:
      
      - This will be the *eSIM backup* number from the previous section.
   - Account > Devices and numbers > Set this device's number: **No number**
   - Voicemail - create a Voicemail greeting
   - Security - enable **Filter Spam**


*Google Voice* requires that the account be created from within the U.S.A.

.. note:: The simplest usage is to DENY any prompts for it to:
   
   - Become the default SMS or Dialer
   - To Forward calls

|logo_googlevoice| Organize
^^^^^^^^^^^^^^^^^^^^^^

Keep track of this new number:
   
   - In Google Contacts, iCloud, etc., a suggested naming convention is ``your_name Me VN GoogleVoice``

.. _virtual-phone-numbers-googlevoice-test:

|logo_googlevoice| Test
^^^^^^^^^^^^^^^^^^^^^^

Call and send a test SMS to/from the new *GoogleVoice* number.

.. _virtual-phone-numbers-essential-recovery:

.. _virtual-phone-numbers-textnow:

|logo_textnow_bg| TextNow
-------------------

.. |logo_textnow_bg| image:: images/virtual_phone_numbers/logo_textnow.png
   :width: 15%

This service is used to send/receive messages and calls.

.. _virtual-phone-numbers-textnow-install:

|logo_textnow| Install
^^^^^^^^^^^^^^^^^^^^^^
   
Install on your smartphone.

If Android, decline the promt to Set *TextNow* as your default calling app

.. note::

   External link: https://www.textnow.com/downloads/

.. _virtual-phone-numbers-textnow-account:

|logo_textnow| Account
^^^^^^^^^^^^^^^^^^^^^^

On the smartphone:

   - Choose Sign Up
   - Choose Sign Up with Email
   - Create an account entry, within *Bitwarden*, save the entry, and copy/paste these credentials into the *TextNow* app.
   - Choose a phone number to use
      
      - Suggestion: choose an area code and region where you have not lived (helps to identify spam).
   - Make an In-App Purchase to Lock in Number with an Annual Subscription ($5 USD).
   - In this *BitWarden* acount entry's Notes section, add a line saying something like: ``VN TextNow your_number`` 

.. _virtual-phone-numbers-textnow-organize:

|logo_textnow| Organize
^^^^^^^^^^^^^^^^^^^^^^

Keep track of this new number:
   
   - In Google Contacts, iCloud, etc., a suggested naming convention is ``your_name Me VN TextNow``

.. _virtual-phone-numbers-textnow-test:

|logo_textnow| Test
^^^^^^^^^^^^^^^^^^^^^^

Call and send a test SMS to/from the new *TextNow* number.

Essential Recovery
------------

Steps for recovery, if/when any or all of your digital devices become inaccessible/lost/stolen or damaged beyond usage:

   - *BitWarden* :ref:`password-manager-essential-recovery`
   - *Virtual Phone Number* :ref:`Primary Virtual Phone Number Recovery <virtual-phone-numbers-choose-primary-provider>`
      
      - Log in

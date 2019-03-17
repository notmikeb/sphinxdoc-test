pybtday
##################


purpose
************
a python bt stack with multi-instance support
a tx and rx async thread 

example
************
device_factory life cycle
   add_factory 
   get_device
   show_devices
   assign_device(id, )
   
device life cycle
   idle
   initing
   inited
   deiniting
   deinited

.. code-block:: python
  GenericDevice
    # (btday_sdk\dut\dev.py)
	self.elmgr = EventLoopMgr(conf.did + '.el')
	self.drv = DrvMgr.get_drv(conf.url)

HciMod // hci module	
   
plan_manager
   run each case_manager, make sure all device state is right
   case_manager   
       run case based

new a bt_stack object and bind it with a transport object

python use zadig 
  `https://zadig.akeo.ie/ <https://zadig.akeo.ie/>`_ - zadig software to install libusb

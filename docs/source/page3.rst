pybtday
##################


purpose
************
a python bt stack with multi-instance support
a tx and rx async thread 



pybluez compatible

1. dependence - pybluez-gap api

2. dependence - l2cap and rfcomm socket factory api

3. dependence - builtin dll files

pybluetooth compatible 

1. dependence - scapy2 

2. dependence - libusb


a whole picture

1.use qpython3 on android device. it is python3.6 version 

`https://github.com/qpython-android/qpython3/releases <qpython3>`_

  
  
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

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 10:42:36 2016

@author: lathropk
"""

def calc_gross_drop(rec):
    gross_drop = rec['MeteredBillIn'] + \
                 rec['BillInVar'] + \
                 rec['MeteredVoucherIn'] + \
                 rec['VoucherInVar']
    return gross_drop

def calc_att_payouts_and_vouchers(rec):
    payouts = rec['ActualAttPaidExtBonus'] - rec['AttPaidExtBonusVar'] + \
              rec['ActualAttPaidCC'] - rec['AttPaidCCVar'] + \
              rec['ActualAttPaidProg'] - rec['AttPaidProgVar'] + \
              rec['ElecTicketOut'] + rec['TicketOutVar'] + \
              rec['JPHandpay']
              
    return payouts
    
def calc_lease_fee(rec):
    if rec['Lease_ID'] == 0:
        return float(rec['ProgPC']) * 1
    elif rec['Lease_ID'] == 1:
        return (float(rec['ProgPC']) * 1) / 30
    elif rec['Lease_ID'] == 2:
        return float(rec['ElecCoinIn']) * (rec['ProgPC'] /100)
    elif rec['Lease_ID'] == 3:
        return float((rec['ManualBillDrop'] + rec['ManualTicketDrop'])) * (rec['ProgPC'] /100)
    elif rec['Lease_ID'] == 4:
        return float(((rec['MeteredBillIn'] + \
                rec['BillInVar'] + \
                rec['MeteredVoucherIn'] + \
                rec['VoucherInVar'] + \
                rec['PtsCashDownElec']) - \
               (rec['Fills'] + \
                rec['ActualAttPaidProg'] + \
                rec['ActualAttPaidExtBonus'] + \
                rec['ActualAttPaidCC'] + \
                rec['Jackpots'] + \
                rec['ManualTicketOut']))) * (rec['ProgPC'] /100)
    else:
        return 0

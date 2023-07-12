s1apic = "100.64.46.11"
s1user = "admin"
s1password = "123Cisco123"

s2apic = "100.64.46.21"
s2user = "admin"
s2password = "123Cisco123"


s1BorderLeaf = {"1201":"LA1", "1202":"LA2", "1203":"LA3", "1204":"LA4"}
s2BorderLeaf = {"1201":"LB1", "1202":"LB2"}


LA1_tenant5_v307_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-5:vrf-5-1515/peer-[10.12.7.10/32]/ent-[10.12.7.10].json?query-target=self"
LA1_tenant5_v307_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-5:vrf-5-1515/peer-[2002::10:12:7:10/128]/ent-[2002::10:12:7:10].json?query-target=self"
LA1_tenant6_v513_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1617/peer-[12.12.13.10/32]/ent-[12.12.13.10].json?query-target=self"
LA1_tenant6_v513_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1617/peer-[2002::12:12:13:10/128]/ent-[2002::12:12:13:10].json?query-target=self"
LA1_tenant6_v704_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1806/peer-[16.16.4.10/32]/ent-[16.16.4.10].json?query-target=self"
LA1_tenant6_v704_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1806/peer-[2002::16:16:4:10/128]/ent-[2002::16:16:4:10].json?query-target=self"

LA2_tenant5_v307_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-5:vrf-5-1515/peer-[10.12.7.10/32]/ent-[10.12.7.10].json?query-target=self"
LA2_tenant5_v307_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-5:vrf-5-1515/peer-[2002::10:12:7:10/128]/ent-[2002::10:12:7:10].json?query-target=self"
LA2_tenant6_v513_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1617/peer-[12.12.13.10/32]/ent-[12.12.13.10].json?query-target=self"
LA2_tenant6_v513_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1617/peer-[2002::12:12:13:10/128]/ent-[2002::12:12:13:10].json?query-target=self"
LA2_tenant6_v704_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1806/peer-[16.16.4.10/32]/ent-[16.16.4.10].json?query-target=self"
LA2_tenant6_v704_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1806/peer-[2002::16:16:4:10/128]/ent-[2002::16:16:4:10].json?query-target=self"


LA3_tenant5_v308_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1203" + \
            "/sys/bgp/inst/dom-tenant-5:vrf-5-1515/peer-[10.12.8.10/32]/ent-[10.12.8.10].json?query-target=self"
LA3_tenant5_v308_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1203" + \
            "/sys/bgp/inst/dom-tenant-5:vrf-5-1515/peer-[2002::10:12:8:10/128]/ent-[2002::10:12:8:10].json?query-target=self"
LA3_tenant6_v515_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1203" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1618/peer-[12.12.15.10/32]/ent-[12.12.15.10].json?query-target=self"
LA3_tenant6_v515_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1203" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1618/peer-[2002::12:12:15:10/128]/ent-[2002::12:12:15:10].json?query-target=self"
LA3_tenant6_v708_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1203" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1812/peer-[16.16.8.10/32]/ent-[16.16.8.10].json?query-target=self"
LA3_tenant6_v708_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1203" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1812/peer-[2002::16:16:8:10/128]/ent-[2002::16:16:8:10].json?query-target=self"

LA4_tenant5_v308_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1204" + \
            "/sys/bgp/inst/dom-tenant-5:vrf-5-1515/peer-[10.12.8.10/32]/ent-[10.12.8.10].json?query-target=self"
LA4_tenant5_v308_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1204" + \
            "/sys/bgp/inst/dom-tenant-5:vrf-5-1515/peer-[2002::10:12:8:10/128]/ent-[2002::10:12:8:10].json?query-target=self"
LA4_tenant6_v515_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1204" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1618/peer-[12.12.15.10/32]/ent-[12.12.15.10].json?query-target=self"
LA4_tenant6_v515_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1204" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1618/peer-[2002::12:12:15:10/128]/ent-[2002::12:12:15:10].json?query-target=self"
LA4_tenant6_v708_v4 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1204" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1812/peer-[16.16.8.10/32]/ent-[16.16.8.10].json?query-target=self"
LA4_tenant6_v708_v6 = "https://" + s1apic + \
            "/api/node/mo/topology/pod-1/node-1204" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1812/peer-[2002::16:16:8:10/128]/ent-[2002::16:16:8:10].json?query-target=self"


LB1_tenant6_v514_v4 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1617/peer-[12.12.14.10/32]/ent-[12.12.14.10].json?query-target=self"
LB1_tenant6_v514_v6 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1617/peer-[2002::12:12:14:10/128]/ent-[2002::12:12:14:10].json?query-target=self"
LB1_tenant6_v516_v4 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1618/peer-[12.12.16.10/32]/ent-[12.12.16.10].json?query-target=self"
LB1_tenant6_v516_v6 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1618/peer-[2002::12:12:16:10/128]/ent-[2002::12:12:16:10].json?query-target=self"
LB1_tenant6_v712_v4 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1818/peer-[16.16.12.10/32]/ent-[16.16.12.10].json?query-target=self"
LB1_tenant6_v712_v6 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1201" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1818/peer-[2002::16:16:12:10/128]/ent-[2002::16:16:12:10].json?query-target=self"

LB2_tenant6_v514_v4 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1617/peer-[12.12.14.10/32]/ent-[12.12.14.10].json?query-target=self"
LB2_tenant6_v514_v6 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1617/peer-[2002::12:12:14:10/128]/ent-[2002::12:12:14:10].json?query-target=self"
LB2_tenant6_v516_v4 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1618/peer-[12.12.16.10/32]/ent-[12.12.16.10].json?query-target=self"
LB2_tenant6_v516_v6 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1618/peer-[2002::12:12:16:10/128]/ent-[2002::12:12:16:10].json?query-target=self"
LB2_tenant6_v712_v4 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1818/peer-[16.16.12.10/32]/ent-[16.16.12.10].json?query-target=self"
LB2_tenant6_v712_v6 = "https://" + s2apic + \
            "/api/node/mo/topology/pod-1/node-1202" + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1818/peer-[2002::16:16:12:10/128]/ent-[2002::16:16:12:10].json?query-target=self"


LA1_bgp_url = [LA1_tenant5_v307_v4, LA1_tenant5_v307_v6, LA1_tenant6_v513_v4, LA1_tenant6_v513_v6, LA1_tenant6_v704_v4, LA1_tenant6_v704_v6]
LA2_bgp_url = [LA2_tenant5_v307_v4, LA2_tenant5_v307_v6, LA2_tenant6_v513_v4, LA2_tenant6_v513_v6, LA2_tenant6_v704_v4, LA2_tenant6_v704_v6]
LA3_bgp_url = [LA3_tenant5_v308_v4, LA3_tenant5_v308_v6, LA3_tenant6_v515_v4, LA3_tenant6_v515_v6, LA3_tenant6_v708_v4, LA3_tenant6_v708_v6]
LA4_bgp_url = [LA4_tenant5_v308_v4, LA4_tenant5_v308_v6, LA4_tenant6_v515_v4, LA4_tenant6_v515_v6, LA4_tenant6_v708_v4, LA4_tenant6_v708_v6]
LB1_bgp_url = [LB1_tenant6_v514_v4, LB1_tenant6_v514_v6, LB1_tenant6_v516_v4, LB1_tenant6_v516_v6, LB1_tenant6_v712_v4, LB1_tenant6_v712_v6]
LB2_bgp_url = [LB2_tenant6_v514_v4, LB2_tenant6_v514_v6, LB2_tenant6_v516_v4, LB2_tenant6_v516_v6, LB2_tenant6_v712_v4, LB2_tenant6_v712_v6]

LA1_bgp_url_dict = {
    "LA1_tenant5_v307_v4": LA1_tenant5_v307_v4,
    "LA1_tenant5_v307_v6": LA1_tenant5_v307_v6,
    "LA1_tenant6_v513_v4": LA1_tenant6_v513_v4,
    "LA1_tenant6_v513_v6": LA1_tenant6_v513_v6,
    "LA1_tenant6_v704_v4": LA1_tenant6_v704_v4,
    "LA1_tenant6_v704_v6": LA1_tenant6_v704_v6
}

LA2_bgp_url_dict = {
    "LA2_tenant5_v307_v4": LA2_tenant5_v307_v4,
    "LA2_tenant5_v307_v6": LA2_tenant5_v307_v6,
    "LA2_tenant6_v513_v4": LA2_tenant6_v513_v4,
    "LA2_tenant6_v513_v6": LA2_tenant6_v513_v6,
    "LA2_tenant6_v704_v4": LA2_tenant6_v704_v4,
    "LA2_tenant6_v704_v6": LA2_tenant6_v704_v6
}

LA3_bgp_url_dict = {
    "LA3_tenant5_v308_v4": LA3_tenant5_v308_v4,
    "LA3_tenant5_v308_v6": LA3_tenant5_v308_v6,
    "LA3_tenant6_v515_v4": LA3_tenant6_v515_v4,
    "LA3_tenant6_v515_v6": LA3_tenant6_v515_v6,
    "LA3_tenant6_v708_v4": LA3_tenant6_v708_v4,
    "LA3_tenant6_v708_v6": LA3_tenant6_v708_v6
}

LA4_bgp_url_dict = {
    "LA4_tenant5_v308_v4": LA4_tenant5_v308_v4,
    "LA4_tenant5_v308_v6": LA4_tenant5_v308_v6,
    "LA4_tenant6_v515_v4": LA4_tenant6_v515_v4,
    "LA4_tenant6_v515_v6": LA4_tenant6_v515_v6,
    "LA4_tenant6_v708_v4": LA4_tenant6_v708_v4,
    "LA4_tenant6_v708_v6": LA4_tenant6_v708_v6
}

LB1_bgp_url_dict = {
    "LB1_tenant6_v514_v4": LB1_tenant6_v514_v4,
    "LB1_tenant6_v514_v6": LB1_tenant6_v514_v6,
    "LB1_tenant6_v516_v4": LB1_tenant6_v516_v4,
    "LB1_tenant6_v516_v6": LB1_tenant6_v516_v6,
    "LB1_tenant6_v712_v4": LB1_tenant6_v712_v4,
    "LB1_tenant6_v712_v6": LB1_tenant6_v712_v6
}

LB2_bgp_url_dict = {
    "LB2_tenant6_v514_v4": LB2_tenant6_v514_v4,
    "LB2_tenant6_v514_v6": LB2_tenant6_v514_v6,
    "LB2_tenant6_v516_v4": LB2_tenant6_v516_v4,
    "LB2_tenant6_v516_v6": LB2_tenant6_v516_v6,
    "LB2_tenant6_v712_v4": LB2_tenant6_v712_v4,
    "LB2_tenant6_v712_v6": LB2_tenant6_v712_v6
}


# rsPath

rsPath_LA12_tenant5_v307_v4 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-5/out-L3OUT-LA12-v307/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-307-v4.json"

rsPath_LA12_tenant5_v307_v6 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-5/out-L3OUT-LA12-v307/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-307-v6.json"

rsPath_LA12_tenant6_v513_v4 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LA12-v513/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-513-v4.json"

rsPath_LA12_tenant6_v513_v6 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LA12-v513/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-513-v6.json"

rsPath_LA12_tenant6_v704_v4 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LA12-v704/lnodep-node-1201-1202/lifp-svi-P3_3-vlan-704-v4.json"
           
rsPath_LA12_tenant6_v704_v6 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LA12-v704/lnodep-node-1201-1202/lifp-svi-P3_3-vlan-704-v6.json"

rsPath_LA34_tenant5_v308_v4 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-5/out-L3OUT-LA34-v308/lnodep-node-1203-1204/lifp-svi-P13_13_2-vlan-308-v4.json"
        
rsPath_LA34_tenant5_v308_v6 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-5/out-L3OUT-LA34-v308/lnodep-node-1203-1204/lifp-svi-P13_13_2-vlan-308-v6.json"

rsPath_LA34_tenant6_v515_v4 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LA34-v515/lnodep-node-1203-1204/lifp-svi-P13_13_2-vlan-515-v4.json"
           
rsPath_LA34_tenant6_v515_v6 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LA34-v515/lnodep-node-1203-1204/lifp-svi-P13_13_2-vlan-515-v6.json"
                   
rsPath_LA34_tenant6_v708_v4 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LA34-v708/lnodep-node-1203-1204/lifp-svi-P3_3_2-vlan-708-v4.json"
               
rsPath_LA34_tenant6_v708_v6 = "https://" + s1apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LA34-v708/lnodep-node-1203-1204/lifp-svi-P3_3_2-vlan-708-v6.json"

rsPath_LB12_tenant6_v514_v4 = "https://" + s2apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LB12-v514/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-514-v4.json"
           
rsPath_LB12_tenant6_v514_v6 = "https://" + s2apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LB12-v514/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-514-v6.json"

rsPath_LB12_tenant6_v516_v4 = "https://" + s2apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LB12-v516/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-516-v4.json"
           
rsPath_LB12_tenant6_v516_v6 = "https://" + s2apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LB12-v516/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-516-v6.json"

rsPath_LB12_tenant6_v712_v4 = "https://" + s2apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LB12-v712/lnodep-node-1201-1202/lifp-svi-P3_3-vlan-712-v4.json"
           
rsPath_LB12_tenant6_v712_v6 = "https://" + s2apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LB12-v712/lnodep-node-1201-1202/lifp-svi-P3_3-vlan-712-v6.json"


rsPath_LA12 = [rsPath_LA12_tenant5_v307_v4, rsPath_LA12_tenant5_v307_v6, rsPath_LA12_tenant6_v513_v4, rsPath_LA12_tenant6_v513_v6, rsPath_LA12_tenant6_v704_v4, rsPath_LA12_tenant6_v704_v6]
rsPath_LA34 = [rsPath_LA34_tenant5_v308_v4, rsPath_LA34_tenant5_v308_v6, rsPath_LA34_tenant6_v515_v4, rsPath_LA34_tenant6_v515_v6, rsPath_LA34_tenant6_v708_v4, rsPath_LA34_tenant6_v708_v6]
rsPath_LB12 = [rsPath_LB12_tenant6_v514_v4, rsPath_LB12_tenant6_v514_v6, rsPath_LB12_tenant6_v516_v4, rsPath_LB12_tenant6_v516_v6, rsPath_LB12_tenant6_v712_v4, rsPath_LB12_tenant6_v712_v6]

rsPath_LA12_tenant5_v307_v4_LocA = "configs/LA12_tenant5_v307_pathA_v4.json"
rsPath_LA12_tenant5_v307_v4_LocB = "configs/LA12_tenant5_v307_pathB_v4.json"
rsPath_LA12_tenant5_v307_v6_LocA = "configs/LA12_tenant5_v307_pathA_v6.json"
rsPath_LA12_tenant5_v307_v6_LocB = "configs/LA12_tenant5_v307_pathB_v6.json"

rsPath_LA12_tenant6_v513_v4_LocA = "configs/LA12_tenant6_v513_pathA_v4.json"
rsPath_LA12_tenant6_v513_v4_LocB = "configs/LA12_tenant6_v513_pathB_v4.json"
rsPath_LA12_tenant6_v513_v6_LocA = "configs/LA12_tenant6_v513_pathA_v6.json"
rsPath_LA12_tenant6_v513_v6_LocB = "configs/LA12_tenant6_v513_pathB_v6.json"

rsPath_LA12_tenant6_v704_v4_LocA = "configs/LA12_tenant6_v704_pathA_v4.json"
rsPath_LA12_tenant6_v704_v4_LocB = "configs/LA12_tenant6_v704_pathB_v4.json"
rsPath_LA12_tenant6_v704_v6_LocA = "configs/LA12_tenant6_v704_pathA_v6.json"
rsPath_LA12_tenant6_v704_v6_LocB = "configs/LA12_tenant6_v704_pathB_v6.json"

rsPath_LA34_tenant5_v308_v4_LocA = "configs/LA34_tenant5_v308_pathA_v4.json"
rsPath_LA34_tenant5_v308_v4_LocB = "configs/LA34_tenant5_v308_pathB_v4.json"
rsPath_LA34_tenant5_v308_v6_LocA = "configs/LA34_tenant5_v308_pathA_v6.json"
rsPath_LA34_tenant5_v308_v6_LocB = "configs/LA34_tenant5_v308_pathB_v6.json"


rsPath_LA34_tenant6_v515_v4_LocA = "configs/LA34_tenant6_v515_pathA_v4.json"
rsPath_LA34_tenant6_v515_v4_LocB = "configs/LA34_tenant6_v515_pathB_v4.json"
rsPath_LA34_tenant6_v515_v6_LocA = "configs/LA34_tenant6_v515_pathA_v6.json"
rsPath_LA34_tenant6_v515_v6_LocB = "configs/LA34_tenant6_v515_pathB_v6.json"

rsPath_LA34_tenant6_v708_v4_LocA = "configs/LA34_tenant6_v708_pathA_v4.json"
rsPath_LA34_tenant6_v708_v4_LocB = "configs/LA34_tenant6_v708_pathB_v4.json"
rsPath_LA34_tenant6_v708_v6_LocA = "configs/LA34_tenant6_v708_pathA_v6.json"
rsPath_LA34_tenant6_v708_v6_LocB = "configs/LA34_tenant6_v708_pathB_v6.json"


rsPath_LB12_tenant6_v514_v4_LocA = "configs/LB12_tenant6_v514_pathA_v4.json"
rsPath_LB12_tenant6_v514_v4_LocB = "configs/LB12_tenant6_v514_pathB_v4.json"
rsPath_LB12_tenant6_v514_v6_LocA = "configs/LB12_tenant6_v514_pathA_v6.json"
rsPath_LB12_tenant6_v514_v6_LocB = "configs/LB12_tenant6_v514_pathB_v6.json"

rsPath_LB12_tenant6_v516_v4_LocA = "configs/LB12_tenant6_v516_pathA_v4.json"
rsPath_LB12_tenant6_v516_v4_LocB = "configs/LB12_tenant6_v516_pathB_v4.json"
rsPath_LB12_tenant6_v516_v6_LocA = "configs/LB12_tenant6_v516_pathA_v6.json"
rsPath_LB12_tenant6_v516_v6_LocB = "configs/LB12_tenant6_v516_pathB_v6.json"

rsPath_LB12_tenant6_v712_v4_LocA = "configs/LB12_tenant6_v712_pathA_v4.json"
rsPath_LB12_tenant6_v712_v4_LocB = "configs/LB12_tenant6_v712_pathB_v4.json"
rsPath_LB12_tenant6_v712_v6_LocA = "configs/LB12_tenant6_v712_pathA_v6.json"
rsPath_LB12_tenant6_v712_v6_LocB = "configs/LB12_tenant6_v712_pathB_v6.json"

#10.12.7.2/24
LA1_tenant5_v307_v4_mem_A = "https://" + s1apic + \
        "/api/mo/uni/tn-tenant-5/out-L3OUT-LA12-v307/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-307-v4/rspathL3OutAtt-[topology/pod-1/protpaths-1201-1202/pathep-[P13_13]]/mem-A.json"
#12.12.13.2/24
LA1_tenant6_v513_v4_mem_A = "https://" + s1apic + \
        "/api/mo/uni/tn-tenant-6/out-L3OUT-LA12-v513/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-513-v4/rspathL3OutAtt-[topology/pod-1/protpaths-1201-1202/pathep-[P13_13]]/mem-A.json"

#16.16.4.2/24
LA1_tenant6_v704_v4_mem_A = "https://" + s1apic + \
        "/api/mo/uni/tn-tenant-6/out-L3OUT-LA12-v704/lnodep-node-1201-1202/lifp-svi-P3_3-vlan-704-v4/rspathL3OutAtt-[topology/pod-1/protpaths-1201-1202/pathep-[P3_3]]/mem-A.json"

#10.12.8.2/24
LA3_tenant5_v308_v4_mem_A = "https://" + s1apic + \
        "/api/mo/uni/tn-tenant-5/out-L3OUT-LA34-v308/lnodep-node-1203-1204/lifp-svi-P13_13_2-vlan-308-v4/rspathL3OutAtt-[topology/pod-1/protpaths-1203-1204/pathep-[P13_13_2]]/mem-A.json"
#12.12.15.2/24
LA3_tenant6_v515_v4_mem_A = "https://" + s1apic + \
        "/api/mo/uni/tn-tenant-6/out-L3OUT-LA34-v515/lnodep-node-1203-1204/lifp-svi-P13_13_2-vlan-515-v4/rspathL3OutAtt-[topology/pod-1/protpaths-1203-1204/pathep-[P13_13_2]]/mem-A.json"
#16.16.8.2/24
LA3_tenant6_v708_v4_mem_A = "https://" + s1apic + \
        "/api/mo/uni/tn-tenant-6/out-L3OUT-LA34-v708/lnodep-node-1203-1204/lifp-svi-P3_3_2-vlan-708-v4/rspathL3OutAtt-[topology/pod-1/protpaths-1203-1204/pathep-[P3_3_2]]/mem-A.json"

#12.12.14.2/24
LB1_tenant6_v514_v4_mem_A = "https://" + s2apic + \
        "/api/mo/uni/tn-tenant-6/out-L3OUT-LB12-v514/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-514-v4/rspathL3OutAtt-[topology/pod-1/protpaths-1201-1202/pathep-[P13_13]]/mem-A.json"

#12.12.16.2/24
LB1_tenant6_v516_v4_mem_A = "https://" + s2apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LB12-v516/lnodep-node-1201-1202/lifp-svi-P13_13-vlan-516-v4/rspathL3OutAtt-[topology/pod-1/protpaths-1201-1202/pathep-[P13_13]]/mem-A.json"

#16.16.12.2/24
LB1_tenant6_v712_v4_mem_A = "https://" + s2apic + \
            "/api/mo/uni/tn-tenant-6/out-L3OUT-LB12-v712/lnodep-node-1201-1202/lifp-svi-P3_3-vlan-712-v4/rspathL3OutAtt-[topology/pod-1/protpaths-1201-1202/pathep-[P3_3]]/mem-A.json"

ipVpcMemberMappingSite1LA12 = {
    "10.12.7.2": LA1_tenant5_v307_v4_mem_A,
    "12.12.13.2": LA1_tenant6_v513_v4_mem_A,
    "16.16.4.2": LA1_tenant6_v704_v4_mem_A
}

ipVpcMemberMappingSite1LA34 = {
    "10.12.8.2": LA3_tenant5_v308_v4_mem_A,
    "12.12.15.2": LA3_tenant6_v515_v4_mem_A,
    "16.16.8.2": LA3_tenant6_v708_v4_mem_A
}

ipVpcMemberMappingSite2LB12 = {
    "12.12.14.2": LB1_tenant6_v514_v4_mem_A,
    "12.12.16.2": LB1_tenant6_v516_v4_mem_A,
    "16.16.12.2": LB1_tenant6_v712_v4_mem_A
}
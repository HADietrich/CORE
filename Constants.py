tech_assist_codes = ["Technical Assist/Fleet Response", "4.1.7", "4.2.2.1", "4.2.2.2", "4.2.2.3", "4.2.2.4.1",
                     "4.2.2.4.2", "4.4.2", "4.4.5.5", "6.1.3.6", "4.4.5"]
instruction_direc_codes = ["Instructions/Directives", "4.4.3", "4.4.4", "4.5.4", "4.5.4.3.1", "4.5.4.3.2", "4.5.4.3.3",
                           "4.5.5"]
IT_Cyber_codes = ["Information Technology/Cyber Security", "5.4.2.1", "5.4.2.2", "5.4.2.3", "6.1.5.2"]
maint_eng_codes = ["Maintenance & Engineering Source Documentation/Performance Analysis", "4.2.1","4.3.1.1","4.3.1.2",
                   "4.3.1.3","4.3.1.4","4.3.1.5","4.3.1.6","4.3.1.7","4.4.1","4.5.3.1","4.5.7"]
mx_source_doc_codes = ["Mx Source Documentation", "6.1.1.2"]
nae_codes = ["NAE Activities", "4.3", "4.3.3","4.3.6"]
product_support_codes = ["Product Support/Engineering Support", "6.2.1.3", "4.5", "4.5.1", "4.5.6.1.10", "4.5.6.1.15",
                         "4.7", "6.1", "6.1.3", "5.4.2", "5.4.2.4", "6.1.5.3"]
software_defect_codes = ["Software Defect Resolution/Release", "5.3.3", "5.3.4", "5.3.5"]
stat_requirements_codes = ["Statutory Requirements", "6.2.2", "3.1.1"]
supply_support_codes = ["Supply Support", "4.2.1.1", "4.5.2.1.1", "4.5.2.1.2", "4.5.2.2", "6.1.1"]

ABC_codes_array = [tech_assist_codes, instruction_direc_codes, IT_Cyber_codes, maint_eng_codes, mx_source_doc_codes, nae_codes,
              product_support_codes, software_defect_codes, stat_requirements_codes, supply_support_codes]


PE_PRR_Dict = {"ARS/EFT PRL": {"STRING": "ARS/EFT PRL", "PMA": "201", "PE": "0204164N"},
               "Crew System PRL": {"STRING": "Crew System PRL", "PMA": "202", "PE": "0204261N"},
               "AE2100 ENG PRL": {"STRING": "AE2100 ENG PRL", "PMA": "207", "PE": "0206127M"},
               "C KC130 PRL": {"STRING": "C KC130 PRL", "PMA": "207", "PE": "0204453N"},
               "Executive Lift PRL": {"STRING": "Executive Lift PRL", "PMA": "207", "PE": "0204214N"},
               "KC130J PRL": {"STRING": "KC130J PRL", "PMA": "207", "PE": "0206127M"},
               "Medium Lift PRL": {"STRING": "Medium Lift PRL", "PMA": "207", "PE": "0204214N"},
               "T56 - SERIES 3 ENGINE PRL": {"STRING": "T56 - SERIES 3 ENGINE PRL", "PMA": "207", "PE": "0206127M"},
               "Utility Lift PRL": {"STRING": "Utility Lift PRL", "PMA": "207", "PE": "0204214N"},
               "MANGL PRL": {"STRING": "MANGL PRL", "PMA": "209", "PE": "0204453N"},
               "ACE PRL": {"STRING": "ACE PRL", "PMA": "209", "PE": "0204453N"},
               "IFF Systems PRL": {"STRING": "IFF Systems PRL", "PMA": "213", "PE": "0204453N"},
               "Commercial A/C Services PRL": {"STRING": "Commercial A/C Services PRL", "PMA": "226", "PE": "0204217N"},
               "F16 PRL": {"STRING": "F16 PRL", "PMA": "226", "PE": "0204633N"},
               "F5 PRL": {"STRING": "F5 PRL", "PMA": "226", "PE": "0204633N"},
               "J85 ENG PRL": {"STRING": "J85 ENG PRL", "PMA": "226", "PE": "0204633N"},
               "TPS PRL": {"STRING": "TPS PRL", "PMA": "226", "PE": "0804771N"},
               "C2 PRL": {"STRING": "C2 PRL", "PMA": "231", "PE": "0204151N"},
               "E2C PRL": {"STRING": "E2C PRL", "PMA": "231", "PE": "0204152N"},
               "E2D PRL": {"STRING": "E2D PRL", "PMA": "231", "PE": "0204152N"},
               "T56 - SERIES 4 ENGINE PRL": {"STRING": "T56 - SERIES 4 ENGINE PRL", "PMA": "231", "PE": "0204152N"},
               "AEA PRL": {"STRING": "AEA PRL", "PMA": "234", "PE": "0204154N"},
               "Intrepid Tiger PRL": {"STRING": "Intrepid Tiger PRL", "PMA": "234", "PE": "0206143M"},
               "NGJ MB PRL": {"STRING": "NGJ MB PRL", "PMA": "234", "PE": "0204154N"},
               "AV8 PRL": {"STRING": "AV8 PRL", "PMA": "257", "PE": "0206110M"},
               "F402 ENG PRL": {"STRING": "F402 ENG PRL", "PMA": "257", "PE": "0206110M"},
               "ATE PRL": {"STRING": "ATE PRL", "PMA": "260", "PE": "0204161N"},
               "CSE PRL": {"STRING": "CSE PRL", "PMA": "260", "PE": "0204161N"},
               "H53 PRL": {"STRING": "H53 PRL", "PMA": "261", "PE": "0206122M"},
               "H53K PRL": {"STRING": "H53K PRL", "PMA": "261", "PE": "0206122M"},
               "T408 ENG PRL": {"STRING": "T408 ENG PRL", "PMA": "261", "PE": "0206122M"},
               "T64 ENG PRL": {"STRING": "T64 ENG PRL", "PMA": "261", "PE": "0206122M"},
               "BEAR TRAP PRL": {"STRING": "BEAR TRAP PRL", "PMA": "264", "PE": "0204453N"},
               "Sonobuoy PRL": {"STRING": "Sonobuoy PRL", "PMA": "264", "PE": "0204453N"},
               "Sonobuoy PRL": {"STRING": "Sonobuoy PRL", "PMA": "264", "PE": "0204453N"},
               "F18A D PRL": {"STRING": "F18A D PRL", "PMA": "265", "PE": "0204136N"},
               "EA18G PRL": {"STRING": "EA18G PRL", "PMA": "265", "PE": "0204269N"},
               "F18E F PRL": {"STRING": "F18E F PRL", "PMA": "265", "PE": "0204136N"},
               "F404 ENG PRL": {"STRING": "F404 ENG PRL", "PMA": "265", "PE": "0204136N"},
               "F414 ENG PRL": {"STRING": "F414 ENG PRL", "PMA": "265", "PE": "0204136N"},
               "EW Systems PRL": {"STRING": "EW Systems PRL", "PMA": "272", "PE": "0204453N"},
               "AHTS PRL": {"STRING": "AHTS PRL", "PMA": "273", "PE": "0804745N"},
               "F405 ENG PRL": {"STRING": "F405 ENG PRL", "PMA": "273", "PE": "0804745N"},
               "T34 PRL": {"STRING": "T34 PRL", "PMA": "273", "PE": "0804745N"},
               "T44 PRL": {"STRING": "T44 PRL", "PMA": "273", "PE": "0804745N"},
               "T45 PRL": {"STRING": "T45 PRL", "PMA": "273", "PE": "0804745N"},
               "T6 JPATS PRL": {"STRING": "T6 JPATS PRL", "PMA": "273", "PE": "0804745N"},
               "TH57 PRL": {"STRING": "TH57 PRL", "PMA": "273", "PE": "0804745N"},
               "VH PRL": {"STRING": "VH PRL", "PMA": "274", "PE": "0901212M"},
               "AE1107 CMV ENG PRL": {"STRING": "AE1107 CMV ENG PRL", "PMA": "275", "PE": "0204151N"},
               "AE1107 ENG PRL": {"STRING": "AE1107 ENG PRL", "PMA": "275", "PE": "0206121M"},
               "CMV22 PRL": {"STRING": "CMV22 PRL", "PMA": "275", "PE": "0204151N"},
               "V22 PRL": {"STRING": "V22 PRL", "PMA": "275", "PE": "0206121M"},
               "H1 PRL": {"STRING": "H1 PRL", "PMA": "276", "PE": "0206131M"},
               "CFM56 ENG PRL": {"STRING": "CFM56 ENG PRL", "PMA": "290", "PE": "0204251N"},
               "Manned Recon Systems PRL": {"STRING": "Manned Recon Systems PRL", "PMA": "290", "PE": "0305207N"},
               "Multi-Intel Sensors PRL": {"STRING": "Multi-Intel Sensors PRL", "PMA": "290", "PE": "0305241N"},
               "P8A PRL": {"STRING": "P8A PRL", "PMA": "290", "PE": "0204251N"},
               "H60 PRL": {"STRING": "H60 PRL", "PMA": "299", "PE": "0204243N"},
               "T700 ENG PRL": {"STRING": "H60 PRL", "PMA": "299", "PE": "0204243N"}
               }


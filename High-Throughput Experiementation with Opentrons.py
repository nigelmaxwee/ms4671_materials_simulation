from opentrons import protocol_api

# metadata
metadata = {
    "protocolName": "My Protocol",
    "author": "Name <opentrons@example.com>",
    "description": "Simple protocol to get started using the OT-2",
}

# requirements
requirements = {"robotType": "OT-2", "apiLevel": "2.13"}

# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # labware
    plate = protocol.load_labware(
        "nest_96_wellplate_200ul_flat", location="1"
    )
    tiprack = protocol.load_labware(
        "opentrons_96_tiprack_300ul", location="10"
    )
    resource = protocol.load_labware(
        "opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", location="6"
    )
    # pipettes
    left_pipette = protocol.load_instrument(
        "p300_single", mount="left", tip_racks=[tiprack]
    )
    # Define max volume in µL
    maxvolume = 300 
    # Initialise count
    count = 0
    # Define the number of rows and columns
    rows = 8
    columns = 12
    # Define our 2d-arrays
    blue_df = [
    [1.0000, 0.9091, 0.8182, 0.7273, 0.6364, 0.5455, 0.4545, 0.3636, 0.2727, 0.1818, 0.0909, 0.0000],
    [0.8571, 0.7792, 0.7013, 0.6234, 0.5455, 0.4675, 0.3896, 0.3117, 0.2338, 0.1558, 0.0779, 0.0000],
    [0.7143, 0.6494, 0.5844, 0.5195, 0.4545, 0.3896, 0.3247, 0.2597, 0.1948, 0.1299, 0.0649, 0.0000],
    [0.5714, 0.5195, 0.4675, 0.4156, 0.3636, 0.3117, 0.2597, 0.2078, 0.1558, 0.1039, 0.0519, 0.0000],
    [0.4286, 0.3896, 0.3506, 0.3117, 0.2727, 0.2338, 0.1948, 0.1558, 0.1169, 0.0779, 0.0390, 0.0000],
    [0.2857, 0.2597, 0.2338, 0.2078, 0.1818, 0.1558, 0.1299, 0.1039, 0.0779, 0.0519, 0.0260, 0.0000],
    [0.1429, 0.1299, 0.1169, 0.1039, 0.0909, 0.0779, 0.0649, 0.0519, 0.0390, 0.0260, 0.0130, 0.0000],
    [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
]
    red_df = [
    [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
    [0.1429, 0.1299, 0.1169, 0.1039, 0.0909, 0.0779, 0.0649, 0.0519, 0.0390, 0.0260, 0.0130, 0.0000],
    [0.2857, 0.2597, 0.2338, 0.2078, 0.1818, 0.1558, 0.1299, 0.1039, 0.0779, 0.0519, 0.0260, 0.0000],
    [0.4286, 0.3896, 0.3506, 0.3117, 0.2727, 0.2338, 0.1948, 0.1558, 0.1169, 0.0779, 0.0390, 0.0000],
    [0.5714, 0.5195, 0.4675, 0.4156, 0.3636, 0.3117, 0.2597, 0.2078, 0.1558, 0.1039, 0.0519, 0.0000],
    [0.7143, 0.6494, 0.5844, 0.5195, 0.4545, 0.3896, 0.3247, 0.2597, 0.1948, 0.1299, 0.0649, 0.0000],
    [0.8571, 0.7792, 0.7013, 0.6234, 0.5455, 0.4675, 0.3896, 0.3117, 0.2338, 0.1558, 0.0779, 0.0000],
    [1.0000, 0.9091, 0.8182, 0.7273, 0.6364, 0.5455, 0.4545, 0.3636, 0.2727, 0.1818, 0.0909, 0.0000]
]
    green_df = [
    [0.0000, 0.0909, 0.1818, 0.2727, 0.3636, 0.4545, 0.5455, 0.6364, 0.7273, 0.8182, 0.9091, 1.0000],
    [0.0000, 0.0779, 0.1558, 0.2338, 0.3117, 0.3896, 0.4675, 0.5455, 0.6234, 0.7013, 0.7792, 0.8571],
    [0.0000, 0.0649, 0.1299, 0.1948, 0.2597, 0.3247, 0.3896, 0.4545, 0.5195, 0.5844, 0.6494, 0.7143],
    [0.0000, 0.0519, 0.1039, 0.1558, 0.2078, 0.2597, 0.3117, 0.3636, 0.4156, 0.4675, 0.5195, 0.5714],
    [0.0000, 0.0390, 0.0779, 0.1169, 0.1558, 0.1948, 0.2338, 0.2727, 0.3117, 0.3506, 0.3896, 0.4286],
    [0.0000, 0.0260, 0.0519, 0.0779, 0.1039, 0.1299, 0.1558, 0.1818, 0.2078, 0.2338, 0.2597, 0.2857],
    [0.0000, 0.0130, 0.0260, 0.0390, 0.0519, 0.0649, 0.0779, 0.0909, 0.1039, 0.1169, 0.1299, 0.1429],
    [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
]
    yellow_df = [
    [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
    [0.0000, 0.0130, 0.0260, 0.0390, 0.0519, 0.0649, 0.0779, 0.0909, 0.1039, 0.1169, 0.1299, 0.1429],
    [0.0000, 0.0260, 0.0519, 0.0779, 0.1039, 0.1299, 0.1558, 0.1818, 0.2078, 0.2338, 0.2597, 0.2857],
    [0.0000, 0.0390, 0.0779, 0.1169, 0.1558, 0.1948, 0.2338, 0.2727, 0.3117, 0.3506, 0.3896, 0.4286],
    [0.0000, 0.0519, 0.1039, 0.1558, 0.2078, 0.2597, 0.3117, 0.3636, 0.4156, 0.4675, 0.5195, 0.5714],
    [0.0000, 0.0649, 0.1299, 0.1948, 0.2597, 0.3247, 0.3896, 0.4545, 0.5195, 0.5844, 0.6494, 0.7143],
    [0.0000, 0.0779, 0.1558, 0.2338, 0.3117, 0.3896, 0.4675, 0.5455, 0.6234, 0.7013, 0.7792, 0.8571],
    [0.0000, 0.0909, 0.1818, 0.2727, 0.3636, 0.4545, 0.5455, 0.6364, 0.7273, 0.8182, 0.9091, 1.0000]
]
    
    # Loop through each color and dispense it across the grid
    for color in ["A3", "A4", "B3", "B4"]: #A3 = blue, A4 = red, B3 = green, B4 = yellow
        left_pipette.pick_up_tip()
        for col in range(columns):
            for row in range(rows):
                
                if color == "A3": #blue
                    if blue_df[row][col]*maxvolume == 0:
                        count += 1
                        continue
                    else:
                        left_pipette.aspirate(blue_df[row][col]*maxvolume, resource[color])
                        left_pipette.dispense(blue_df[row][col]*maxvolume, plate.wells()[count])
                        count += 1
                                              
                if color == "A4": #red
                    if red_df[row][col]*maxvolume == 0:
                        count += 1
                        continue
                    else:                                    
                        left_pipette.aspirate(red_df[row][col]*maxvolume, resource[color])
                        left_pipette.dispense(red_df[row][col]*maxvolume, plate.wells()[count])
                        count += 1
                                              
                if color == "B3": #green
                    if green_df[row][col]*maxvolume == 0:
                        count += 1
                        continue
                    else:
                        left_pipette.aspirate(green_df[row][col]*maxvolume, resource[color])
                        left_pipette.dispense(green_df[row][col]*maxvolume, plate.wells()[count])
                        count += 1
                                              
                if color == "B4": #yellow
                    if yellow_df[row][col]*maxvolume == 0:
                        count += 1
                        continue
                    else:
                        left_pipette.aspirate(yellow_df[row][col]*maxvolume, resource[color])
                        left_pipette.dispense(yellow_df[row][col]*maxvolume, plate.wells()[count])
                        count += 1
                                              
        count = 0
        left_pipette.drop_tip()


 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        div_row1 = Button(description='---Initialization Options--', disabled=True, layout=divider_button_layout)

        param_name2 = Button(description='multiplicity_of_infection', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.multiplicity_of_infection = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name3 = Button(description='use_single_infected_cell', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.use_single_infected_cell = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Drug induced maximum damage on rates---', disabled=True, layout=divider_button_layout)

        param_name4 = Button(description='drug_ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'lightgreen'

        self.drug_ACE2_endocytosis_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name5 = Button(description='drug_virion_export', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'tan'

        self.drug_virion_export = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name6 = Button(description='drug_ACE2_binding_rate', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'lightgreen'

        self.drug_ACE2_binding_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name7 = Button(description='drug_virion_uncoated', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'tan'

        self.drug_virion_uncoated = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name8 = Button(description='drug_uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'lightgreen'

        self.drug_uncoated_to_RNA_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='drug_protein_synthesis_rate', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'tan'

        self.drug_protein_synthesis_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name10 = Button(description='drug_virion_assembly_rate', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'lightgreen'

        self.drug_virion_assembly_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Pharmacodynamics model parameters ---', disabled=True, layout=divider_button_layout)

        param_name11 = Button(description='drug_doses', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'tan'

        self.drug_doses = FloatText(
          value=5.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='EC_50', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'lightgreen'

        self.EC_50 = FloatText(
          value=2.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='Hill_power', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'tan'

        self.Hill_power = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='drug_efficiency', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'lightgreen'

        self.drug_efficiency = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='dose_duration', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'tan'

        self.dose_duration = IntText(
          value=14400000,
          step=1000000,
          style=style, layout=widget_layout)

        param_name16 = Button(description='start_inject', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'lightgreen'

        self.start_inject = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='internalization_rate', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'tan'

        self.internalization_rate = FloatText(
          value=0.0116,
          step=0.001,
          style=style, layout=widget_layout)

        param_name18 = Button(description='drug_endo_export', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'lightgreen'

        self.drug_endo_export = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name19 = Button(description='drug_binding_replication', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'tan'

        self.drug_binding_replication = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        div_row4 = Button(description='---Cell Color Options--', disabled=True, layout=divider_button_layout)

        param_name20 = Button(description='color_variable', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'lightgreen'

        self.color_variable = Text(
          value='assembled_virion',
          style=style, layout=widget_layout)

        param_name21 = Button(description='apoptotic_epithelium_color', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'tan'

        self.apoptotic_epithelium_color = Text(
          value='black',
          style=style, layout=widget_layout)

        div_row5 = Button(description='---Cell fusion Options--', disabled=True, layout=divider_button_layout)

        param_name22 = Button(description='max_apoptosis_half_max_orginal', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'lightgreen'

        self.max_apoptosis_half_max_orginal = FloatText(
          value=500,
          step=10,
          style=style, layout=widget_layout)

        param_name23 = Button(description='half_max_cell_fusion', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'tan'

        self.half_max_cell_fusion = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name24 = Button(description='drug_fusion_power', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'lightgreen'

        self.drug_fusion_power = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name25 = Button(description='drug_cell_fusion', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'tan'

        self.drug_cell_fusion = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'lightgreen'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'
        units_button8 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'lightgreen'
        units_button9 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'tan'
        units_button12 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='uM', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='uM', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'tan'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'lightgreen'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'tan'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='virion', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='virion', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='multiplicity of infection: virions/cells at t=0' , tooltip='multiplicity of infection: virions/cells at t=0', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='Infect center cell with one virion (overrides MOI)' , tooltip='Infect center cell with one virion (overrides MOI)', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button15 = Button(description='ACE2 receptor-virus endocytosis rate with drug' , tooltip='ACE2 receptor-virus endocytosis rate with drug', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='rate at which a virion is exported from a live cell with drug' , tooltip='rate at which a virion is exported from a live cell with drug', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='ACE2 receptor-virus binding rate with drug' , tooltip='ACE2 receptor-virus binding rate with drug', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='rate at which uncoated virion makes its mRNA available with drug' , tooltip='rate at which uncoated virion makes its mRNA available with drug', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='rate at which uncoated virion makes its mRNA available with drug' , tooltip='rate at which uncoated virion makes its mRNA available with drug', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='rate at mRNA creates complete set of proteins with drug' , tooltip='rate at mRNA creates complete set of proteins with drug', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='rate at which viral proteins are assembled into complete virion with drug' , tooltip='rate at which viral proteins are assembled into complete virion with drug', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='The injected drug concentration' , tooltip='The injected drug concentration', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='Drug concentration value that gives 50% max effect' , tooltip='Drug concentration value that gives 50% max effect', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='Power that used in Hill Function for calculating drug effect' , tooltip='Power that used in Hill Function for calculating drug effect', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='Drug efficiency on inhibition of virion multiplication ([0, 1])' , tooltip='Drug efficiency on inhibition of virion multiplication ([0, 1])', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='The time duration between two dose injection' , tooltip='The time duration between two dose injection', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='Time that first dose injection' , tooltip='Time that first dose injection', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='Rate at which lung epithelium uptakes drug' , tooltip='Rate at which lung epithelium uptakes drug', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='Turn on the drug effect on virial endocytosis and export or not' , tooltip='Turn on the drug effect on virial endocytosis and export or not', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='Turn on the drug effect on virial binding and replication or not' , tooltip='Turn on the drug effect on virial binding and replication or not', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='color cells based on this variable' , tooltip='color cells based on this variable', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='apoptotic epithelial cell color' , tooltip='apoptotic epithelial cell color', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='viral load at which cells reach half max apoptosis rate' , tooltip='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='viral load at which cell fusion reach half max rate' , tooltip='viral load at which cell fusion reach half max rate', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='Power that used in function for cell fusion inhibtion' , tooltip='Power that used in function for cell fusion inhibtion', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='Turn on the drug effect on cell fusion or not' , tooltip='Turn on the drug effect on cell fusion or not', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.multiplicity_of_infection, units_button3, desc_button2] 
        row3 = [param_name3, self.use_single_infected_cell, units_button4, desc_button3] 
        row15 = [param_name4, self.drug_ACE2_endocytosis_rate, units_button6, desc_button15] 
        row16 = [param_name5, self.drug_virion_export, units_button7, desc_button16] 
        row17 = [param_name6, self.drug_ACE2_binding_rate, units_button8, desc_button17] 
        row18 = [param_name7, self.drug_virion_uncoated, units_button9, desc_button18] 
        row19 = [param_name8, self.drug_uncoated_to_RNA_rate, units_button10, desc_button19] 
        row20 = [param_name9, self.drug_protein_synthesis_rate, units_button11, desc_button20] 
        row21 = [param_name10, self.drug_virion_assembly_rate, units_button12, desc_button21] 
        row22 = [param_name11, self.drug_doses, units_button14, desc_button22] 
        row23 = [param_name12, self.EC_50, units_button15, desc_button23] 
        row24 = [param_name13, self.Hill_power, units_button16, desc_button24] 
        row25 = [param_name14, self.drug_efficiency, units_button17, desc_button25] 
        row26 = [param_name15, self.dose_duration, units_button18, desc_button26] 
        row27 = [param_name16, self.start_inject, units_button19, desc_button27] 
        row28 = [param_name17, self.internalization_rate, units_button20, desc_button28] 
        row29 = [param_name18, self.drug_endo_export, units_button21, desc_button29] 
        row30 = [param_name19, self.drug_binding_replication, units_button22, desc_button30] 
        row31 = [param_name20, self.color_variable, units_button24, desc_button31] 
        row32 = [param_name21, self.apoptotic_epithelium_color, units_button25, desc_button32] 
        row33 = [param_name22, self.max_apoptosis_half_max_orginal, units_button27, desc_button33] 
        row34 = [param_name23, self.half_max_cell_fusion, units_button28, desc_button34] 
        row35 = [param_name24, self.drug_fusion_power, units_button29, desc_button35] 
        row36 = [param_name25, self.drug_cell_fusion, units_button30, desc_button36] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)

        self.tab = VBox([
          box1,
          div_row1,
          box2,
          box3,
          div_row2,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          div_row3,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          div_row4,
          box31,
          box32,
          div_row5,
          box33,
          box34,
          box35,
          box36,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.multiplicity_of_infection.value = float(uep.find('.//multiplicity_of_infection').text)
        self.use_single_infected_cell.value = ('true' == (uep.find('.//use_single_infected_cell').text.lower()) )
        self.drug_ACE2_endocytosis_rate.value = float(uep.find('.//drug_ACE2_endocytosis_rate').text)
        self.drug_virion_export.value = float(uep.find('.//drug_virion_export').text)
        self.drug_ACE2_binding_rate.value = float(uep.find('.//drug_ACE2_binding_rate').text)
        self.drug_virion_uncoated.value = float(uep.find('.//drug_virion_uncoated').text)
        self.drug_uncoated_to_RNA_rate.value = float(uep.find('.//drug_uncoated_to_RNA_rate').text)
        self.drug_protein_synthesis_rate.value = float(uep.find('.//drug_protein_synthesis_rate').text)
        self.drug_virion_assembly_rate.value = float(uep.find('.//drug_virion_assembly_rate').text)
        self.drug_doses.value = float(uep.find('.//drug_doses').text)
        self.EC_50.value = float(uep.find('.//EC_50').text)
        self.Hill_power.value = float(uep.find('.//Hill_power').text)
        self.drug_efficiency.value = float(uep.find('.//drug_efficiency').text)
        self.dose_duration.value = int(uep.find('.//dose_duration').text)
        self.start_inject.value = int(uep.find('.//start_inject').text)
        self.internalization_rate.value = float(uep.find('.//internalization_rate').text)
        self.drug_endo_export.value = ('true' == (uep.find('.//drug_endo_export').text.lower()) )
        self.drug_binding_replication.value = ('true' == (uep.find('.//drug_binding_replication').text.lower()) )
        self.color_variable.value = (uep.find('.//color_variable').text)
        self.apoptotic_epithelium_color.value = (uep.find('.//apoptotic_epithelium_color').text)
        self.max_apoptosis_half_max_orginal.value = float(uep.find('.//max_apoptosis_half_max_orginal').text)
        self.half_max_cell_fusion.value = float(uep.find('.//half_max_cell_fusion').text)
        self.drug_fusion_power.value = float(uep.find('.//drug_fusion_power').text)
        self.drug_cell_fusion.value = ('true' == (uep.find('.//drug_cell_fusion').text.lower()) )


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//multiplicity_of_infection').text = str(self.multiplicity_of_infection.value)
        uep.find('.//use_single_infected_cell').text = str(self.use_single_infected_cell.value)
        uep.find('.//drug_ACE2_endocytosis_rate').text = str(self.drug_ACE2_endocytosis_rate.value)
        uep.find('.//drug_virion_export').text = str(self.drug_virion_export.value)
        uep.find('.//drug_ACE2_binding_rate').text = str(self.drug_ACE2_binding_rate.value)
        uep.find('.//drug_virion_uncoated').text = str(self.drug_virion_uncoated.value)
        uep.find('.//drug_uncoated_to_RNA_rate').text = str(self.drug_uncoated_to_RNA_rate.value)
        uep.find('.//drug_protein_synthesis_rate').text = str(self.drug_protein_synthesis_rate.value)
        uep.find('.//drug_virion_assembly_rate').text = str(self.drug_virion_assembly_rate.value)
        uep.find('.//drug_doses').text = str(self.drug_doses.value)
        uep.find('.//EC_50').text = str(self.EC_50.value)
        uep.find('.//Hill_power').text = str(self.Hill_power.value)
        uep.find('.//drug_efficiency').text = str(self.drug_efficiency.value)
        uep.find('.//dose_duration').text = str(self.dose_duration.value)
        uep.find('.//start_inject').text = str(self.start_inject.value)
        uep.find('.//internalization_rate').text = str(self.internalization_rate.value)
        uep.find('.//drug_endo_export').text = str(self.drug_endo_export.value)
        uep.find('.//drug_binding_replication').text = str(self.drug_binding_replication.value)
        uep.find('.//color_variable').text = str(self.color_variable.value)
        uep.find('.//apoptotic_epithelium_color').text = str(self.apoptotic_epithelium_color.value)
        uep.find('.//max_apoptosis_half_max_orginal').text = str(self.max_apoptosis_half_max_orginal.value)
        uep.find('.//half_max_cell_fusion').text = str(self.half_max_cell_fusion.value)
        uep.find('.//drug_fusion_power').text = str(self.drug_fusion_power.value)
        uep.find('.//drug_cell_fusion').text = str(self.drug_cell_fusion.value)

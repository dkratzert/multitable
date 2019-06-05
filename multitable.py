# -*- coding: utf-8 -*-
from pathlib import Path

from docx import Document
from docx.shared import Pt
import itertools as it
import os
import re

# compiled with "Py -3 -m PyInstaller multitable.spec --onefile"
from cif.fileparser import Cif


def grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=fillvalue)

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

files = list()
for f in os.listdir('./'):
   if f.endswith('.cif'):
       files.append(f)

nfiles = [i.rstrip('.cif') for i in files]    # remove file suffix for display
gfiles=list(grouper(nfiles, 3))               # group in threes to fit on A4 page

document = Document()
style = document.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(10)

strHead='Structure Tables'
str1Par='\nFormatting by user needed: font for symbols, table cell widths!'
str2Par='\nPLEASE DOUBLE-CHECK ALL ENTRIES, CIF FILES CAN BE INCOMPLETE!!!'
str3Par='\nParsed files:\n\n' + "\n".join(files)

document.add_heading(strHead)
document.add_paragraph(str1Par)
document.add_paragraph(str2Par)
document.add_paragraph(str3Par)

document.add_page_break()

slist = (
    ['_chemical_formula_weight',1],
    ['_diffrn_ambient_temperature',2],
    ['_space_group_crystal_system',3],
    ['_space_group_name_H-M_alt',4],
    ['_cell_length_a',5],
    ['_cell_length_b',6],
    ['_cell_length_c',7],
    ['_cell_angle_alpha',8],
    ['_cell_angle_beta',9],
    ['_cell_angle_gamma',10],
    ['_cell_volume',11],
    ['_cell_formula_units_Z',12],
    ['_exptl_crystal_density_diffrn',13],
    ['_exptl_absorpt_coefficient_mu',14],
    ['_exptl_crystal_F_000',15],
    ['_exptl_crystal_size_max',16],
    ['_exptl_crystal_size_mid',16],
    ['_exptl_crystal_size_min',16],
    ['_exptl_crystal_colour',17],
    ['_exptl_crystal_description',18],
    ['_diffrn_radiation_type',19],
    ['_diffrn_radiation_wavelength',19],
    ['_diffrn_reflns_theta_min',20],
    ['_diffrn_reflns_theta_max',20],
    ['_diffrn_reflns_limit_h_min',21],
    ['_diffrn_reflns_limit_h_max',21],
    ['_diffrn_reflns_limit_k_min',21],
    ['_diffrn_reflns_limit_k_max',21],
    ['_diffrn_reflns_limit_l_min',21],
    ['_diffrn_reflns_limit_l_max',21],
    ['_diffrn_reflns_number',22],
    ['_reflns_number_total',23],
    ['_diffrn_reflns_av_R_equivalents',23],
    ['_diffrn_reflns_av_unetI/netI',23],
    ['_refine_ls_number_reflns',24],
    ['_refine_ls_number_restraints',24],
    ['_refine_ls_number_parameters',24],
    ['_refine_ls_goodness_of_fit_ref',25],
    ['_refine_ls_R_factor_gt',26],
    ['_refine_ls_wR_factor_gt',26], 
    ['_refine_ls_R_factor_all',27],
    ['_refine_ls_wR_factor_ref',27], 
    ['_refine_diff_density_max',28],
    ['_refine_diff_density_min',28] 
)

lstindex = len(gfiles)-1 
for page in enumerate(gfiles):                             # one page per three structures:
    document.add_paragraph('')                             # cannot format cells directly,
    paragraph = document.paragraphs[-1]                    # but it will keep settings from
    paragraph_format = style.paragraph_format              # previous paragraph -> dirty hack:
    paragraph_format.space_before = Pt(4)                  # create paragraph, apply style,
    paragraph_format.space_after = Pt(0)                   # kill paragraph, create table.
    p = paragraph._element                                 
    p.getparent().remove(p)
    p._p = p._element = None
    table = document.add_table(rows=1, cols=4)
    hdr_cells = table.rows[0].cells
    content=list()

    #setup table format:
    for i in range(0,29):
        row = table.add_row() # define row and cells separately
        row_cells = row.cells
        for j in range(0,3):
            row_cells[j].style = document.styles['Normal']

    #populate description column:
    lgnd1 = table.cell(1, 0).paragraphs[0]
    lgnd1sub = lgnd1.add_run('Empirical formula')
    lgnd2 = table.cell(2, 0).paragraphs[0]
    lgnd2sub = lgnd2.add_run('Formula weight')
    lgnd3 = table.cell(3, 0).paragraphs[0]
    lgnd3sub = lgnd3.add_run('Temperature/K')
    lgnd4 = table.cell(4, 0).paragraphs[0]
    lgnd4sub = lgnd4.add_run('Crystal system')
    lgnd5 = table.cell(5, 0).paragraphs[0]
    lgnd5sub = lgnd5.add_run('Space group')
    lgnd6 = table.cell(6, 0).paragraphs[0]
    lgnd6sub = lgnd6.add_run('a/\u212B')
    lgnd7 = table.cell(7, 0).paragraphs[0]
    lgnd7sub = lgnd7.add_run('b/\u212B')
    lgnd8 = table.cell(8, 0).paragraphs[0]
    lgnd8sub = lgnd8.add_run('c/\u212B')
    lgnd9 = table.cell(9, 0).paragraphs[0]
    lgnd9sub = lgnd9.add_run('\u03B1/\u00b0')
    lgnd10 = table.cell(10, 0).paragraphs[0]
    lgnd10sub = lgnd10.add_run('\u03B2/\u00b0')
    lgnd11 = table.cell(11, 0).paragraphs[0]
    lgnd11sub = lgnd11.add_run('\u03B3/\u00b0')
    lgnd12 = table.cell(12, 0).paragraphs[0]
    lgnd12sub = lgnd12.add_run('Volume/\u212B')
    lgnd12sub1 = lgnd12.add_run('3')
    lgnd12sub1.font.superscript = True
    lgnd13 = table.cell(13, 0).paragraphs[0]
    lgnd13sub = lgnd13.add_run('Z')
    lgnd13sub.font.italic = True
    lgnd14 = table.cell(14, 0).paragraphs[0]
    lgnd14sub = lgnd14.add_run('\u03C1')
    lgnd14sub1 = lgnd14.add_run('calc')
    lgnd14sub1.font.subscript = True
    lgnd14sub2 = lgnd14.add_run(' g/cm')
    lgnd14sub3 = lgnd14.add_run('3')
    lgnd14sub3.font.superscript = True
    lgnd15 = table.cell(15, 0).paragraphs[0]
    lgnd15sub = lgnd15.add_run('\u03BC/mm')
    lgnd15sub1 = lgnd15.add_run('-1')
    lgnd15sub1.font.superscript = True
    lgnd16 = table.cell(16, 0).paragraphs[0]
    lgnd16sub = lgnd16.add_run('F')
    lgnd16sub.font.italic = True
    lgnd16sub1 = lgnd16.add_run('(000)')
    lgnd17 = table.cell(17, 0).paragraphs[0]
    lgnd17sub = lgnd17.add_run('Crystal size/mm')
    lgnd17sub1 = lgnd17.add_run('3')
    lgnd17sub1.font.superscript = True
    lgnd18 = table.cell(18, 0).paragraphs[0]
    lgnd18sub = lgnd18.add_run('Crystal colour')
    lgnd19 = table.cell(19, 0).paragraphs[0]
    lgnd19sub = lgnd19.add_run('Crystal shape')
    lgnd20 = table.cell(20, 0).paragraphs[0]
    lgnd20sub = lgnd20.add_run('Radiation')
    lgnd21 = table.cell(21, 0).paragraphs[0]
    lgnd21sub = lgnd21.add_run('2\u03F4 range/\u00b0')
    lgnd22 = table.cell(22, 0).paragraphs[0]
    lgnd22sub = lgnd22.add_run('Index ranges')
    lgnd23 = table.cell(23, 0).paragraphs[0]
    lgnd23sub = lgnd23.add_run('Reflections collected')
    lgnd24 = table.cell(24, 0).paragraphs[0]
    lgnd24sub = lgnd24.add_run('Independent reflections')
    lgnd25 = table.cell(25, 0).paragraphs[0]
    lgnd25sub = lgnd25.add_run('Data/Restraints/Parameters')
    lgnd26 = table.cell(26, 0).paragraphs[0]
    lgnd26sub = lgnd26.add_run('Goodness-of-fit on ')
    lgnd26sub1 = lgnd26.add_run('F')
    lgnd26sub1.font.italic = True
    lgnd26sub2 = lgnd26.add_run('2')
    lgnd26sub2.font.superscript = True    
    lgnd27 = table.cell(27, 0).paragraphs[0]
    lgnd27sub = lgnd27.add_run('Final ')
    lgnd27sub1 = lgnd27.add_run('R')
    lgnd27sub1.font.italic = True
    lgnd27sub2 = lgnd27.add_run(' indexes [')
    lgnd27sub3 = lgnd27.add_run('I')
    lgnd27sub3.font.italic = True
    lgnd27sub4 = lgnd27.add_run('\u22652\u03C3(')
    lgnd27sub5 = lgnd27.add_run('I')
    lgnd27sub5.font.italic = True
    lgnd27sub3 = lgnd27.add_run(')]')
    lgnd28 = table.cell(28, 0).paragraphs[0]
    lgnd28sub = lgnd28.add_run('Final ')
    lgnd28sub1 = lgnd28.add_run('R')
    lgnd28sub1.font.italic = True
    lgnd28sub2 = lgnd28.add_run(' indexes [all data]')
    lgnd29 = table.cell(29, 0).paragraphs[0]
    lgnd29sub = lgnd29.add_run('Largest peak/hole /e\u212B')
    lgnd29sub1 = lgnd29.add_run('3')
    lgnd29sub1.font.superscript = True

    for j in range(0,3):
        if page[1][j] is not None:
            filename=page[1][j]+'.cif'
            with open(filename, 'r') as f:
                cif = Cif()
                cif.parsefile(f.readlines())
                print(cif.cif_data['_chemical_formula_sum'])

            with open(filename, 'r') as file:
                ltext='no Formula'
                lsg='no SG'
                lsize1=''
                lsize2=''
                lsize3=''
                lrad=''
                lres1=''
                lres2=''
                lhkl1=''
                lhkl2=''
                lhkl3=''
                lhkl4=''
                lhkl5=''
                lhkl6=''
                lrint1=''
                lrint2=''
                lrint3=''
                ldat1=''
                ldat2=''
                ldat3=''
                lr2s1=''
                lr2s2=''
                lrfull1=''
                lrfull2=''
                lhole1=''
                lhole2=''
                """
                cif = Cif()
                cif.parsefile(file.readlines())
                if cif.cif_data['_chemical_formula_sum']:
                    formrunsub = formrun.add_run(cif.cif_data['_chemical_formula'])
                """
                
                for line in file:
                    ### FORMULA:
                    if line.startswith('_chemical_formula_sum'):
                        ltext = line.strip('_chemical_formula_sum').lstrip().rstrip().strip("'").rstrip("\n\r")   # this works
                        ltext2 = ltext.replace(" ", "")
                        ltext3 = [''.join(x[1]) for x in it.groupby(ltext2, lambda x: x.isalpha())]
                        for i in range(0,len(ltext3)):
                            formrun = table.cell(1, j+1).paragraphs[0]
                            formrunsub = formrun.add_run(ltext3[i])
                            if isfloat(ltext3[i]):
                                formrunsub.font.subscript = True
                    ### ALL UNPROBLEMATIC ENTRIES TREATED THE SAME (-> slist):
                    for i in range(0,len(slist)):
                        if line.split(' ')[0] == slist[i][0]:
                            value = line.strip(slist[i][0]).lstrip().rstrip().strip("'").rstrip("\n\r")
                            ### SMALLER HACKS:
                            if slist[i][0] == '_space_group_name_H-M_alt':
                                if len(value) > 4:                      # don't modify P 1
                                    value = re.sub(r'\s1','',value)     # remove extra Hall "1" for mono and tric
                                value = re.sub(r'\s','',value)          # remove all remaining whitespace
                                lsg = value                             # formatted for console output
                                sgtext = [char for char in value] 
                                for k in range(0,len(sgtext)):
                                    sgrun = table.cell(slist[i][1]+1, j+1).paragraphs[0]
                                    sgrunsub = sgrun.add_run(sgtext[k])
                                    if not sgtext[k].isdigit():                        
                                        sgrunsub.font.italic = True
                                    else:
                                        if sgtext[k-1].isdigit():
                                            sgrunsub.font.subscript = True      # lowercase the second digit if previous is also digit
                                #table.cell(slist[i][1]+1, j+1).text = value
                            elif slist[i][0] == '_exptl_crystal_size_max':
                                lsize1 = value
                                break
                            elif slist[i][0] == '_exptl_crystal_size_mid':
                                lsize2 = value
                                break 
                            elif slist[i][0] == '_exptl_crystal_size_min':
                                lsize3 = value
                                break
                            elif slist[i][0] == '_diffrn_radiation_type':
                                lrad = value.replace('\\a','\u03b1').replace('\\b','\u03b2')
                                break
                            elif slist[i][0] == '_diffrn_radiation_wavelength':
                                lrad = lrad + ' (\u03bb=' + value +')'
                                value = lrad
                                value = value.replace(" ", "")
                                valuep = value.partition("K")
                                radrun = table.cell(slist[i][1]+1, j+1).paragraphs[0]
                                radrun.add_run(valuep[0])
                                radrunita = radrun.add_run(valuep[1])
                                radrunita.font.italic = True
                                radrun.add_run(valuep[2])
                                break
                            elif slist[i][0] == '_diffrn_reflns_theta_min':
                                lres1 = value
                                break
                            elif slist[i][0] == '_diffrn_reflns_theta_max':
                                lres2 = value
                                break                                                            
                            elif slist[i][0] == '_diffrn_reflns_limit_h_min':
                                lhkl1 = value
                                break
                            elif slist[i][0] == '_diffrn_reflns_limit_h_max':
                                lhkl2 = value
                                break
                            elif slist[i][0] == '_diffrn_reflns_limit_k_min':
                                lhkl3 = value
                                break
                            elif slist[i][0] == '_diffrn_reflns_limit_k_max':
                                lhkl4 = value
                                break
                            elif slist[i][0] == '_diffrn_reflns_limit_l_min':
                                lhkl5 = value
                                break
                            elif slist[i][0] == '_diffrn_reflns_limit_l_max':
                                lhkl6 = value
                                break                                                                                                     
                            elif slist[i][0] == '_reflns_number_total':
                                lrint1 = value
                                break   
                            elif slist[i][0] == '_diffrn_reflns_av_R_equivalents':
                                lrint2 = value
                                break   
                            elif slist[i][0] == '_diffrn_reflns_av_unetI/netI':
                                lrint3 = value
                                break
                            elif slist[i][0] == '_refine_ls_number_reflns':
                                ldat1 = value
                                break                                   
                            elif slist[i][0] == '_refine_ls_number_restraints':
                                ldat2 = value
                                break             
                            elif slist[i][0] == '_refine_ls_number_parameters':
                                ldat3 = value
                                break                                             
                            elif slist[i][0] == '_refine_ls_R_factor_gt':
                                lr2s1 = value
                                break             
                            elif slist[i][0] == '_refine_ls_wR_factor_gt':
                                lr2s2 = value
                                break                                             
                            elif slist[i][0] == '_refine_ls_R_factor_all':
                                lrfull1 = value
                                break             
                            elif slist[i][0] == '_refine_ls_wR_factor_ref':
                                lrfull2 = value
                                break         
                            elif slist[i][0] == '_refine_diff_density_max':
                                lhole1 = "{0:.2f}".format(round(float(value),2))
                                break             
                            elif slist[i][0] == '_refine_diff_density_min':
                                lhole2 = "{0:.2f}".format(round(float(value),2))
                                break       
                            else:
                                table.cell(slist[i][1]+1, j+1).text = value
                                break
                            break
                ### now prepare & write all the concatenated & derived cell contents:            
                table.cell(17, j+1).text = lsize1 + '\u00d7' + lsize2 + '\u00d7' + lsize3
                table.cell(21, j+1).text = "{0:.2f}".format(2*float(lres1)) + ' to ' + "{0:.2f}".format(2*float(lres2))
                table.cell(22, j+1).text = lhkl1 + ' \u2264 h \u2264 ' + lhkl2 + '\n' + lhkl3 + ' \u2264 k \u2264 ' + lhkl4 + '\n' + lhkl5 + ' \u2264 l \u2264 ' + lhkl6
                rintrun = table.cell(24, j+1).paragraphs[0]
                rintrun.add_run(lrint1 + '\n')
                rintita1 = rintrun.add_run('R')
                rintita1.font.italic = True
                rintsub1 = rintrun.add_run('int')
                rintsub1.font.subscript = True
                rintrun.add_run(' = ' + lrint2 + '\n')
                rintita2 = rintrun.add_run('R')
                rintita2.font.italic = True
                rintsub2 = rintrun.add_run('sigma')
                rintsub2.font.subscript = True
                rintrun.add_run(' = ' + lrint3)
                table.cell(25, j+1).text = ldat1 + '/' + ldat2 + '/' + ldat3
                r2sigrun = table.cell(27, j+1).paragraphs[0]
                r2sigita1 = r2sigrun.add_run('R')
                r2sigita1.font.italic = True
                r2sigsub1 = r2sigrun.add_run('1')
                r2sigsub1.font.subscript = True
                r2sigrun.add_run(' = ' + lr2s1 + '\nw')
                r2sigita2 = r2sigrun.add_run('R')
                r2sigita2.font.italic = True
                r2sigsub2 = r2sigrun.add_run('2')
                r2sigsub2.font.subscript = True
                r2sigrun.add_run(' = ' + lr2s2)
                rfullrun = table.cell(28, j+1).paragraphs[0]
                rfullita1 = rfullrun.add_run('R')
                rfullita1.font.italic = True
                rfullsub1 = rfullrun.add_run('1')
                rfullsub1.font.subscript = True
                rfullrun.add_run(' = ' + lrfull1 + '\nw')
                rfullita2 = rfullrun.add_run('R')
                rfullita2.font.italic = True
                rfullsub2 = rfullrun.add_run('2')
                rfullsub2.font.subscript = True
                rfullrun.add_run(' = ' + lrfull2)
                table.cell(29, j+1).text = lhole1 + '/' + lhole2
                print('File parsed: '+filename+'  ('+ltext+')  '+lsg)

    for i in enumerate(hdr_cells):
        if i[0] < 3 and page[1][i[0]] is not None:
            j=i[0]+1
            hdr_cells[j].text = page[1][i[0]]
    # page break between tables:
    if page[0] < lstindex:
        document.add_page_break()

print('\nScript finished - output file: multitable.docx')
document.save('multitable.docx')

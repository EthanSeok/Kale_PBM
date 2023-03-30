import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import os


def length2var_figure(lai, output_dir):
    fig1, ax1 = plt.subplots()
    lai = lai[lai['leaf_area'] != 988]
    sns.regplot(x=lai['leaf_length'], y=lai['leaf_area'], data=lai, line_kws={'color': 'red'}, scatter_kws={'alpha': 0.5}, order=2, color='black')
    r, p = sp.stats.pearsonr(lai['leaf_length'], lai['leaf_area'])
    # ax1 = plt.gca()
    # ax1.text(.95, .2, 'R2={:.2f}, p={:.2g}'.format(r, p), bbox=dict(facecolor='gray', alpha=0.5),
    #          transform=ax1.transAxes, ha='right', va='center')
    ax1.set_title('Leaf length & Leaf Area')
    ax1.set_ylabel('Leaf Area ($mm^2$)')
    ax1.set_xlabel('Leaf Length ($cm$)')
    ax1.text(.95, .1, '0.8047$eachLen^2$ - 0.3319eachLen',transform=ax1.transAxes, ha='right', va='center')
    fig1.savefig(f"{output_dir}/Leaf length_Leaf Area.png")


def oberved_lai_figure(lai, output_dir):
    fig2, ax2 = plt.subplots()
    colors = "#31a354"
    colors = "#252525"
    sns.scatterplot(x=lai['leafnumber_range2'], y=lai['LAI'], data=lai, marker='s', color=colors, s=65)
    ax2.set_title('LAI observed')
    ax2.set_xlabel('Leaf Number')
    fig2.savefig(f"{output_dir}/LAI observed.png")


def eachLenDist_a_figure(lai, output_dir):
    fig3, ax3 = plt.subplots()
    sns.lineplot(x=lai['leafnumber_range2'] ,y=lai['eachLenDist_a'], data=lai, color='black')
    ax3.set_title('eachLenDist_a')
    fig3.savefig(f"{output_dir}/eachLenDist_a.png")


def eachLenDist_b_figure(lai, output_dir):
    fig4, ax4 = plt.subplots()
    sns.lineplot(x=lai['leafnumber_range2'] ,y=lai['eachLenDist_b'], data=lai, color='black')
    ax4.set_title('eachLenDist_b')
    fig4.savefig(f"{output_dir}/eachLenDist_b.png")


def eachLen_figure(lai, output_dir):
    fig5, ax5 = plt.subplots()
    number1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # plt.plot(lai[lai['leafnumber_range2'] == 2]['eachLen'].values, label='2', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 3]['eachLen'].values, label='3', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 4]['eachLen'].values, label='4', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 5]['eachLen'].values, label='5', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 6]['eachLen'].values, label='6', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 7]['eachLen'].values, label='7', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 8]['eachLen'].values, label='8', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 9]['eachLen'].values, label='9', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 10]['eachLen'].values, label='10', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 11]['eachLen'].values, label='11', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 12]['eachLen'].values, label='12', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 13]['eachLen'].values, label='13', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 14]['eachLen'].values, label='14', linewidth=2.5, marker='.')
    ax5.set_xlabel('Leaf Number')
    ax5.set_title('eachLen')
    ax5.set_ylabel('eachLen ($mm^2$)')
    ax5.set_xticks( number ,number1)
    ax5.legend(title='Leaf Number', loc='upper right', ncol=2)
    fig5.savefig(f"{output_dir}/eachLen.png")



def lai_pred_figure(lai, output_dir):
    fig6, ax6 = plt.subplots()
    colors = "#31a354"
    colors = "#252525"
    sns.scatterplot(x=lai['leafnumber_range2'], y=lai['LAI_expect'], marker='s', color=colors, s=65)
    ax6.set_title('LAI predict')
    ax6.set_ylabel('LAI Predict')
    ax6.set_xlabel('Leaf Number')
    fig6.savefig(f"{output_dir}/LAI predict.png")


def eachLeafArea(lai, output_dir):
    fig7, ax7 = plt.subplots()
    number1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # plt.plot(lai[lai['leafnumber_range2'] == 2]['eachLeafArea'].values, label='2', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 3]['eachLeafArea'].values, label='3', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 4]['eachLeafArea'].values, label='4', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 5]['eachLeafArea'].values, label='5', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 6]['eachLeafArea'].values, label='6', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 7]['eachLeafArea'].values, label='7', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 8]['eachLeafArea'].values, label='8', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 9]['eachLeafArea'].values, label='9', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 10]['eachLeafArea'].values, label='10', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 11]['eachLeafArea'].values, label='11', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 12]['eachLeafArea'].values, label='12', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 13]['eachLeafArea'].values, label='13', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 14]['eachLeafArea'].values, label='14', linewidth=2.5, marker='.')
    ax7.set_xlabel('Leaf Number')
    ax7.set_title('eachLeafArea')
    ax7.set_ylabel('eachLeafArea ($mm^2$)')
    ax7.set_xticks( number ,number1)
    ax7.legend(title='Leaf Number', loc='upper right', ncol=2)
    fig7.savefig(f"{output_dir}/eachLeafArea.png")


def lai_corr_figure(lai, output_dir):
    fig8, ax8 = plt.subplots()
    sns.regplot(x='LAI_expect', y='LAI', data=lai, line_kws={'color': 'red'}, scatter_kws={'s':60,'color':'black'}, marker='s')
    ax8.text(.95, .2, 'R2={}'.format(0.9871), bbox=dict(facecolor='gray', alpha=0.5),
             transform=ax8.transAxes, ha='right', va='center')
    ax8.set_xlabel('LAI Predict ($mm^2$)')
    ax8.set_ylabel('LAI Observed ($mm^2$)')
    ax8.set_title('LAI Corr')
    fig8.savefig(f"{output_dir}/LAI Corr.png")


def leafarea_figure(lai, output_dir):
    fig9, ax9 = plt.subplots()
    colors = "#31a354"
    colors = "#252525"
    sns.scatterplot(x='leafnumber_range2', y='LeafArea', data=lai, marker='s', color=colors, s=65)
    ax9.set_title('LeafArea')
    ax9.set_xlabel('Leaf Number')
    ax9.set_ylabel('LeafArea ($mm^2$)')
    fig9.savefig(f"{output_dir}/LeafArea.png")


def lai_comp(lai, output_dir):
    fig10, ax10 = plt.subplots()
    colors = ["#252525", '#3182bd']
    sns.lineplot(x=lai['leafnumber_range2'], y=lai['LAI_expect'], color=colors[0], label='predict', linewidth=2)
    sns.scatterplot(x=lai['leafnumber_range2'], y=lai['LAI'], data=lai, marker='^', color=colors[1], s=100, label='observed')
    ax10.set_title('LAI Compare')
    ax10.set_ylabel('LAI ($mm^2$)')
    ax10.set_xlabel('Leaf Number')
    ax10.legend()
    fig10.savefig(f"{output_dir}/LAI_compare.png")

def eachLen_before6(lai, output_dir):
    fig11, ax11 = plt.subplots()
    number1 = ['1', '2', '3', '4', '5', '6']
    number = [0, 1, 2, 3, 4, 5]
    number2 = [0, 1, 2, 3, 4, 5, 6]
    plt.plot(lai[lai['leafnumber_range2'] == 3]['eachLen'].values, label='3', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 4]['eachLen'].values, label='4', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 5]['eachLen'].values, label='5', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 6]['eachLen'].values, label='6', linewidth=2.5, marker='.')
    ax11.set_xlabel('Leaf Number')
    ax11.set_title('eachLen before 6')
    ax11.set_ylabel('eachLen ($cm$)')
    ax11.set_xticks( number ,number1)
    ax11.set_yticks(number2)
    ax11.legend(title='Leaf Number', loc='upper right', ncol=2)
    fig11.savefig(f"{output_dir}/eachLen_before_6.png")

def eachLen_after6(lai, output_dir):
    fig12, ax12 = plt.subplots()
    number1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    number2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    plt.plot(lai[lai['leafnumber_range2'] == 7]['eachLen'].values, label='7', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 8]['eachLen'].values, label='8', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 9]['eachLen'].values, label='9', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 10]['eachLen'].values, label='10', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 11]['eachLen'].values, label='11', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 12]['eachLen'].values, label='12', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 13]['eachLen'].values, label='13', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 14]['eachLen'].values, label='14', linewidth=2.5, marker='.')
    ax12.set_xlabel('Leaf Number')
    ax12.set_title('eachLen after 6')
    ax12.set_ylabel('eachLen ($cm$)')
    ax12.set_xticks( number ,number1)
    ax12.set_yticks(number2)
    ax12.legend(title='Leaf Number', loc='upper right', ncol=2)
    fig12.savefig(f"{output_dir}/eachLen_after_6.png")

def main():
    lai = pd.read_csv('kale_lai_v2.csv')
    output_dir = "../output/lai_v2/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    length2var_figure(lai, output_dir)
    oberved_lai_figure(lai, output_dir)
    eachLenDist_a_figure(lai, output_dir)
    eachLenDist_b_figure(lai, output_dir)
    eachLen_figure(lai, output_dir)
    lai_pred_figure(lai, output_dir)
    eachLeafArea(lai, output_dir)
    lai_corr_figure(lai, output_dir)
    leafarea_figure(lai, output_dir)
    lai_comp(lai, output_dir)
    eachLen_before6(lai, output_dir)
    eachLen_after6(lai, output_dir)

if __name__=='__main__':
    main()
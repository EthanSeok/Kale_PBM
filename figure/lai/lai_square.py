import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import os


def length2var_figure(lai, output_dir):
    fig1, ax1 = plt.subplots()
    sns.regplot(x=lai['leaf_length'], y=lai['leaf_area'], data=lai, line_kws={'color': 'red'}, scatter_kws={'alpha': 0.5}, order=2, color='black')
    r, p = sp.stats.pearsonr(lai['leaf_length'], lai['leaf_area'])
    # ax1 = plt.gca()
    # ax1.text(.95, .2, 'R2={:.2f}, p={:.2g}'.format(r, p), bbox=dict(facecolor='gray', alpha=0.5),
    #          transform=ax1.transAxes, ha='right', va='center')
    ax1.set_title('Leaf length & Leaf Area')
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
    number1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    plt.plot(lai[lai['leafnumber_range2'] == 2]['eachLen'].values, label='2', linewidth=2.5, marker='.')
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
    plt.plot(lai[lai['leafnumber_range2'] == 15]['eachLen'].values, label='15', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 16]['eachLen'].values, label='16', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 17]['eachLen'].values, label='17', linewidth=2.5, marker='.')
    ax5.set_xlabel('Leaf Number')
    ax5.set_title('eachLen')
    ax5.set_ylabel('eachLen')
    ax5.set_xticks( number ,number1)
    ax5.legend(title='Leaf Number', loc='center right', ncol=2)
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
    number1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    plt.plot(lai[lai['leafnumber_range2'] == 2]['eachLeafArea'].values, label='2', linewidth=2.5, marker='.')
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
    plt.plot(lai[lai['leafnumber_range2'] == 15]['eachLeafArea'].values, label='15', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 16]['eachLeafArea'].values, label='16', linewidth=2.5, marker='.')
    plt.plot(lai[lai['leafnumber_range2'] == 17]['eachLeafArea'].values, label='17', linewidth=2.5, marker='.')
    ax7.set_xlabel('Leaf Number')
    ax7.set_title('eachLeafArea')
    ax7.set_ylabel('eachLeafArea')
    ax7.set_xticks( number ,number1)
    ax7.legend(title='Leaf Number', loc='center right', ncol=2)
    fig7.savefig(f"{output_dir}/eachLeafArea.png")


def lai_corr_figure(lai, output_dir):
    fig8, ax8 = plt.subplots()
    sns.regplot(x='LAI_expect', y='LAI', data=lai, line_kws={'color': 'red'}, scatter_kws={'s':60,'color':'black'}, marker='s')
    ax8.text(.95, .2, 'R2={}'.format(0.9871), bbox=dict(facecolor='gray', alpha=0.5),
             transform=ax8.transAxes, ha='right', va='center')
    ax8.set_xlabel('LAI Predict')
    ax8.set_ylabel('LAI Observed')
    ax8.set_title('LAI Corr')
    fig8.savefig(f"{output_dir}/LAI Corr.png")


def leafarea_figure(lai, output_dir):
    fig9, ax9 = plt.subplots()
    colors = "#31a354"
    colors = "#252525"
    sns.scatterplot(x='leafnumber_range2', y='LeafArea', data=lai, marker='s', color=colors, s=65)
    ax9.set_title('LeafArea')
    ax9.set_xlabel('Leaf Number')
    ax9.set_ylabel('LeafArea')
    fig9.savefig(f"{output_dir}/LeafArea.png")


def lai_comp(lai, output_dir):
    fig10, ax10 = plt.subplots()
    colors = ["#252525", '#3182bd']
    sns.scatterplot(x=lai['leafnumber_range2'], y=lai['LAI_expect'], marker='s', color=colors[0], s=65, label='predict')
    sns.scatterplot(x=lai['leafnumber_range2'], y=lai['LAI'], data=lai, marker='^', color=colors[1], s=65, label='observed')
    ax10.set_title('LAI Compare')
    ax10.set_ylabel('LAI Predict')
    ax10.set_xlabel('Leaf Number')
    ax10.legend()
    fig10.savefig(f"{output_dir}/LAI_compare.png")


def main():
    lai = pd.read_csv('kale_lai_square.csv')
    output_dir = "../output/lai/직사각형 피팅"
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

if __name__=='__main__':
    main()
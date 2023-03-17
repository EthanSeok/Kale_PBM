import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import os


def c18_figure(env, output_dir):
    fig1, ax1 = plt.subplots()
    c18 = env[(env['temp'] == 18) | (env['temp'] == 17) ]
    c18 = c18[~((c18['DAP'] == 14) & (c18['leaf_cnt'] < 7) & (c18['leaf_cnt'] > 1))]
    sns.regplot(x='DAP', y='leaf_cnt', data=c18, line_kws={'color': 'red'}, scatter_kws={'alpha': 0.5})
    r, p = sp.stats.pearsonr(c18['DAP'], c18['leaf_cnt'])
    ax1 = plt.gca()
    ax1.text(.95, .2, 'R2={:.2f}, p={:.2g}'.format(r, p), bbox=dict(facecolor='gray', alpha=0.5),
            transform=ax1.transAxes, ha='right', va='center')
    ax1.set_title('18°C Leaf Number')
    fig1.savefig(f"{output_dir}/18°C_leaf_number.png")


def c21_figure(env, output_dir):
    fig2, ax2 = plt.subplots()
    c21 = env[env['temp'] == 21]
    sns.regplot(x='DAP', y='leaf_cnt', data=c21, line_kws={'color': 'red'}, scatter_kws={'alpha': 0.5})
    r, p = sp.stats.pearsonr(c21['DAP'], c21['leaf_cnt'])
    ax2 = plt.gca()
    ax2.text(.95, .2, 'R2={:.2f}, p={:.2g}'.format(r, p), bbox=dict(facecolor='gray', alpha=0.5),
            transform=ax2.transAxes, ha='right', va='center')
    plt.title('21°C Leaf Number')
    fig2.savefig(f"{output_dir}/21°C_leaf_number.png")


def c24_figure(env, output_dir):
    fig3, ax3 = plt.subplots()
    c24 = env[env['temp'] == 24]
    sns.regplot(x='DAP', y='leaf_cnt', data=c24, line_kws={'color': 'red'}, scatter_kws={'alpha': 0.5})
    r, p = sp.stats.pearsonr(c24['DAP'], c24['leaf_cnt'])
    ax3 = plt.gca()
    ax3.text(.95, .2, 'R2={:.2f}, p={:.2g}'.format(r, p), bbox=dict(facecolor='gray', alpha=0.5),
            transform=ax3.transAxes, ha='right', va='center')
    plt.title('24°C Leaf Number')
    fig3.savefig(f"{output_dir}/24°C_leaf_number.png")


def GDD_figure(env, output_dir):
    fig4, ax4 = plt.subplots()
    sns.regplot(x='GDD', y='leaf_incr_count', data=env, color='orange', line_kws={'color': 'red'}, scatter_kws={'alpha': 0.5})
    r, p = sp.stats.pearsonr(env['GDD'], env['leaf_incr_count'])
    ax4 = plt.gca()
    ax4.text(.95, .15, 'R2={:.2f}, p={:.2g}'.format(r, p), bbox=dict(facecolor='gray', alpha=0.5),
            transform=ax4.transAxes, ha='right', va='center')
    plt.title('GDD Leaf Increase')
    fig4.savefig(f"{output_dir}/GDD Leaf Increase.png")


def sigmoid_figure(env, output_dir):
    fig5, ax5 = plt.subplots()
    colors = ["#fec44f", "#31a354"]
    sns.scatterplot(x='GDD', y='leaf_incr_count', data=env, color=colors[0], label='leaf_incr_count')
    sns.scatterplot(x='GDD', y='est_inc_leaf', data=env, color=colors[1], label='est_inc_leaf')
    ax5.set_title('sigmoid')
    ax5.set_ylabel('Leaf Number')
    ax5.legend()
    fig5.savefig(f"{output_dir}/sigmoid.png")

def c18_model_figure(env, ln18, output_dir):
    fig6, ax6 = plt.subplots()
    colors = ["#fec44f", "#31a354"]
    c18 = env[(env['temp'] == 18) | (env['temp'] == 17) ]
    c18 = c18[~((c18['DAP'] == 14) & (c18['leaf_cnt'] < 7) & (c18['leaf_cnt'] > 1))]
    sns.scatterplot(x='DAP', y='leaf_cnt', data=c18, color=colors[0], label='observed')
    sns.scatterplot(x='DAP', y='LN', data=ln18, marker='s', color=colors[1], label='predict')
    ax6.set_ylabel('Leaf Number')
    ax6.legend()
    ax6.set_title('18°C Model Leaf Number')
    fig6.savefig(f"{output_dir}/18°C Model Leaf Number.png")


def c21_model_figure(env, ln21, output_dir):
    fig7, ax7 = plt.subplots()
    colors = ["#fec44f", "#31a354"]
    c21 = env[env['temp'] == 21]
    sns.scatterplot(x='DAP', y='leaf_cnt', data=c21, color=colors[0], label='observed')
    sns.scatterplot(x='DAP', y='LN', data=ln21, marker='s', color=colors[1], label='predict')
    ax7.set_ylabel('Leaf Number')
    ax7.legend()
    ax7.set_title('21°C Model Leaf Number')
    fig7.savefig(f"{output_dir}/21°C Model Leaf Number.png")


def c24_model_figure(env, ln24, output_dir):
    fig8, ax8 = plt.subplots()
    colors = ["#fec44f", "#31a354"]
    c24 = env[env['temp'] == 24]
    sns.scatterplot(x='DAP', y='leaf_cnt', data=c24, color=colors[0], label='observed')
    sns.scatterplot(x='DAP', y='LN', data=ln24, marker='s', color=colors[1], label='predict')
    ax8.set_ylabel('Leaf Number')
    ax8.legend()
    ax8.set_title('24°C Model Leaf Number')
    fig8.savefig(f"{output_dir}/24°C Model Leaf Number.png")


def main():
    env = pd.read_csv('kale_env.csv', parse_dates=['date'])
    ln18 = pd.read_csv('18_leaf_number.csv')
    ln21 = pd.read_csv('21_leaf_number.csv')
    ln24 = pd.read_csv('24_leaf_number.csv')

    output_dir = "../output/leaf_number_increase"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    c18_figure(env, output_dir)
    c21_figure(env, output_dir)
    c24_figure(env, output_dir)
    GDD_figure(env, output_dir)
    sigmoid_figure(env,output_dir)
    c18_model_figure(env, ln18, output_dir)
    c21_model_figure(env, ln21, output_dir)
    c24_model_figure(env, ln24, output_dir)

if __name__=='__main__':
    main()
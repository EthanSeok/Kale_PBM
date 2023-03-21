import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import os


def DAP_figure(env, output_dir):
    fig0, ax0 = plt.subplots()
    color=['#41ab5d', '#4eb3d3', '#08589e']
    sns.scatterplot(x='DAP', y='leaf_incr_count', data=env[env['temp1'] == 18], legend=False, s=65, style='temp1', label='18°C', color=color[2], markers='o')
    sns.scatterplot(x='DAP', y='leaf_incr_count', data=env[env['temp1'] == 21], legend=False, s=65, style='temp1', label='21°C', color=color[1], markers='s')
    sns.scatterplot(x='DAP', y='leaf_incr_count', data=env[env['temp1'] == 24], legend=False, s=65, style='temp1', label='24°C', color=color[0], markers='^')
    sns.regplot(x='DAP', y='leaf_incr_count', data=env[env['temp1'] == 24], line_kws={'color': color[0], 'linewidth':2}, scatter_kws={'alpha': 0.5}, scatter=False, ci=None)
    sns.regplot(x='DAP', y='leaf_incr_count', data=env[env['temp1'] == 18], line_kws={'color': color[2], 'linewidth':2}, scatter_kws={'alpha': 0.5}, scatter=False, ci=None)
    sns.regplot(x='DAP', y='leaf_incr_count', data=env[env['temp1'] == 21], line_kws={'color': color[1], 'linewidth':2}, scatter_kws={'alpha': 0.5}, scatter=False, ci=None)

    r, p = sp.stats.pearsonr(env['GDD'], env['leaf_incr_count'])
    ax0 = plt.gca()
    # ax0.text(.95, .15, 'R2={:.2f}, p={:.2g}'.format(r, p), bbox=dict(facecolor='gray', alpha=0.5),
    #         transform=ax0.transAxes, ha='right', va='center')
    norm = plt.Normalize(env['temp1'].min(), env['temp1'].max())
    sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm)
    sm.set_array([])
    # cbar = ax0.figure.colorbar(sm)
    # cbar.set_ticks([18, 21, 24])
    # cbar.set_label("Temp")
    ax0.legend(title='Temp', loc='upper left')
    ax0.set_title('DAP Leaf Increase')
    fig0.savefig(f"{output_dir}/DAP Leaf Increase.png")


def c18_figure(env, output_dir):
    fig1, ax1 = plt.subplots()
    c18 = env[(env['temp'] == 18) | (env['temp'] == 17) ]
    c18 = c18[~((c18['DAP'] == 14) & (c18['leaf_cnt'] < 7) & (c18['leaf_cnt'] > 1))]
    sns.regplot(x='DAP', y='leaf_cnt', data=c18, line_kws={'color': '#252525'}, scatter_kws={'s':50, 'color':'#034e7b'}, marker='s')
    r, p = sp.stats.pearsonr(c18['DAP'], c18['leaf_cnt'])
    ax1 = plt.gca()
    # ax1.text(.95, .2, 'R2={:.4f}'.format(r), bbox=dict(facecolor='gray', alpha=0.5),
    #         transform=ax1.transAxes, ha='right', va='center')
    ax1.set_title('18°C Leaf Number')
    fig1.savefig(f"{output_dir}/18°C_leaf_number.png")


def c21_figure(env, output_dir):
    fig2, ax2 = plt.subplots()
    c21 = env[env['temp'] == 21]
    sns.regplot(x='DAP', y='leaf_cnt', data=c21, line_kws={'color': '#252525'}, scatter_kws={'s':50, 'color':'#034e7b'}, marker='s')
    r, p = sp.stats.pearsonr(c21['DAP'], c21['leaf_cnt'])
    ax2 = plt.gca()
    # ax2.text(.95, .2, 'R2={:.4f}'.format(r), bbox=dict(facecolor='gray', alpha=0.5),
    #         transform=ax2.transAxes, ha='right', va='center')
    plt.title('21°C Leaf Number')
    fig2.savefig(f"{output_dir}/21°C_leaf_number.png")


def c24_figure(env, output_dir):
    fig3, ax3 = plt.subplots()
    c24 = env[env['temp'] == 24]
    sns.regplot(x='DAP', y='leaf_cnt', data=c24, line_kws={'color': '#252525'}, scatter_kws={'s':50, 'color':'#034e7b'}, marker='s')
    r, p = sp.stats.pearsonr(c24['DAP'], c24['leaf_cnt'])
    ax3 = plt.gca()
    # ax3.text(.95, .2, 'R2={:.4f}'.format(r), bbox=dict(facecolor='gray', alpha=0.5),
    #         transform=ax3.transAxes, ha='right', va='center')
    plt.title('24°C Leaf Number')
    fig3.savefig(f"{output_dir}/24°C_leaf_number.png")


def GDD_figure(env, output_dir):
    fig4, ax4 = plt.subplots()
    color=['#41ab5d', '#4eb3d3', '#08589e']
    sns.scatterplot(x='GDD', y='leaf_incr_count', data=env[env['temp1'] == 18], legend=False, s=65, style='temp1', label='18°C', color=color[2], markers='o')
    sns.scatterplot(x='GDD', y='leaf_incr_count', data=env[env['temp1'] == 21], legend=False, s=65, style='temp1', label='21°C', color=color[1], markers='s')
    sns.scatterplot(x='GDD', y='leaf_incr_count', data=env[env['temp1'] == 24], legend=False, s=65, style='temp1', label='24°C', color=color[0], markers='^')
    sns.regplot(x='GDD', y='leaf_incr_count', data=env[env['temp1'] == 24], line_kws={'color': color[0], 'linewidth':2}, scatter_kws={'alpha': 0.5}, scatter=False, ci=None)
    sns.regplot(x='GDD', y='leaf_incr_count', data=env[env['temp1'] == 18], line_kws={'color': color[2], 'linewidth':2}, scatter_kws={'alpha': 0.5}, scatter=False, ci=None)
    sns.regplot(x='GDD', y='leaf_incr_count', data=env[env['temp1'] == 21], line_kws={'color': color[1], 'linewidth':2}, scatter_kws={'alpha': 0.5}, scatter=False, ci=None)

    r, p = sp.stats.pearsonr(env['GDD'], env['leaf_incr_count'])
    ax0 = plt.gca()
    # ax0.text(.95, .15, 'R2={:.2f}, p={:.2g}'.format(r, p), bbox=dict(facecolor='gray', alpha=0.5),
    #         transform=ax0.transAxes, ha='right', va='center')
    norm = plt.Normalize(env['temp1'].min(), env['temp1'].max())
    sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm)
    sm.set_array([])
    # cbar = ax0.figure.colorbar(sm)
    # cbar.set_ticks([18, 21, 24])
    # cbar.set_label("Temp")
    ax4.legend(title='Temp', loc='upper left')
    ax4.set_title('GDD Leaf Increase')
    fig4.savefig(f"{output_dir}/GDD Leaf Increase.png")


def sigmoid_figure(env, output_dir):
    fig5, ax5 = plt.subplots()
    color = "#006837"
    sns.scatterplot(x='GDD', y='leaf_incr_count', data=env, hue='temp1', legend = False, palette='YlOrBr', s=60)
    sns.scatterplot(x='GDD', y='est_inc_leaf', data=env, label='est_inc_leaf', color=color, s=30)
    ax5.set_title('sigmoid')
    ax5.set_ylabel('Leaf Number')
    norm = plt.Normalize(env['temp1'].min(), env['temp1'].max())
    sm = plt.cm.ScalarMappable(cmap='YlOrBr', norm=norm)
    sm.set_array([])
    ax5.figure.colorbar(sm)
    fig5.savefig(f"{output_dir}/sigmoid1.png")


def c18_model_figure(env, ln18, output_dir):
    fig6, ax6 = plt.subplots()
    colors = ["#41ae76", "#034e7b"]
    c18 = env[(env['temp'] == 18) | (env['temp'] == 17) ]
    c18 = c18[~((c18['DAP'] == 14) & (c18['leaf_cnt'] < 7) & (c18['leaf_cnt'] > 1))]
    sns.scatterplot(x='DAP', y='leaf_cnt', data=c18, color=colors[1], label='observed', s=60, marker='s')
    sns.lineplot(x='DAP', y='LN', data=ln18, color=colors[0], label='predict', linewidth=3)
    ax6.set_ylabel('Leaf Number')
    ax6.legend()
    ax6.set_title('18°C Model Leaf Number')
    fig6.savefig(f"{output_dir}/18°C Model Leaf Number.png")


def c21_model_figure(env, ln21, output_dir):
    fig7, ax7 = plt.subplots()
    colors = ["#41ae76", "#034e7b"]
    c21 = env[env['temp'] == 21]
    sns.scatterplot(x='DAP', y='leaf_cnt', data=c21, color=colors[1], label='observed', s=60, marker='s')
    sns.lineplot(x='DAP', y='LN', data=ln21, color=colors[0], label='predict', linewidth=3)
    ax7.set_ylabel('Leaf Number')
    ax7.legend()
    ax7.set_title('21°C Model Leaf Number')
    fig7.savefig(f"{output_dir}/21°C Model Leaf Number.png")


def c24_model_figure(env, ln24, output_dir):
    fig8, ax8 = plt.subplots()
    colors = ["#41ae76", "#034e7b"]
    c24 = env[env['temp'] == 24]
    sns.scatterplot(x='DAP', y='leaf_cnt', data=c24, color=colors[1], label='observed', s=60, marker='s')
    sns.lineplot(x='DAP', y='LN', data=ln24, color=colors[0], label='predict', linewidth=3)
    ax8.set_ylabel('Leaf Number')
    ax8.legend()
    ax8.set_title('24°C Model Leaf Number')
    fig8.savefig(f"{output_dir}/24°C Model Leaf Number.png")


def model_result(env, ln18, ln21, ln24, output_dir):
    fig9, ax9 = plt.subplots(ncols=3, sharey=True, sharex=True,figsize=(15, 5))
    colors = ["#41ae76", "#034e7b"]
    c18 = env[(env['temp'] == 18) | (env['temp'] == 17) ]
    c18 = c18[~((c18['DAP'] == 14) & (c18['leaf_cnt'] < 7) & (c18['leaf_cnt'] > 1))]
    sns.scatterplot(x='DAP', y='leaf_cnt', data=c18, color=colors[1], label='observed', s=60, marker='s', legend=False, ax=ax9[0])
    sns.lineplot(x='DAP', y='LN', data=ln18, color=colors[0], label='predict', linewidth=3, ax=ax9[0])
    ax9[0].set_ylabel('Leaf Number')
    ax9[0].set(ylim=(0, 18))
    ax9[0].set(xlim=(0, 60))
    # ax9[0].get_legend().remove()
    ax9[0].set_xlabel('DAP ($day$)')
    ax9[0].set_title('18°C Model Leaf Number')

    c21 = env[env['temp'] == 21]
    c21 = c21[c21['DAP'] != 0]
    sns.scatterplot(x='DAP', y='leaf_cnt', data=c21, color=colors[1], label='observed', s=60, marker='s', legend=False, ax=ax9[1])
    sns.lineplot(x='DAP', y='LN', data=ln21, color=colors[0], label='predict', linewidth=3, ax=ax9[1])
    ax9[1].set(ylabel=None)
    ax9[1].set(ylim=(0, 18))
    ax9[1].set(xlim=(0, 60))
    ax9[1].get_legend().remove()
    ax9[1].set_xlabel('DAP ($day$)')
    ax9[1].set_title('21°C Model Leaf Number')

    c24 = env[env['temp'] == 24]
    c24 = c24[c24['DAP'] != 0]
    sns.scatterplot(x='DAP', y='leaf_cnt', data=c24, color=colors[1], label='observed', s=60, marker='s', legend=False, ax=ax9[2])
    sns.lineplot(x='DAP', y='LN', data=ln24, color=colors[0], label='predict', linewidth=3, ax=ax9[2])
    ax9[2].set(ylim=(0, 18))
    ax9[2].set(xlim=(0, 60))
    ax9[2].set(ylabel=None)
    ax9[2].set_title('24°C Model Leaf Number')
    ax9[2].set_xlabel('DAP ($day$)')
    ax9[2].get_legend().remove()
    fig9.tight_layout()
    fig9.savefig(fname=f'{output_dir}/model_results.png', bbox_inches='tight', pad_inches=0.2)


def main():
    env = pd.read_csv('kale_env.csv', parse_dates=['date'])
    ln18 = pd.read_csv('18_leaf_number.csv')
    ln21 = pd.read_csv('21_leaf_number.csv')
    ln24 = pd.read_csv('24_leaf_number.csv')

    output_dir = "../output/leaf_number_increase"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    DAP_figure(env, output_dir)
    c18_figure(env, output_dir)
    c21_figure(env, output_dir)
    c24_figure(env, output_dir)
    GDD_figure(env, output_dir)
    sigmoid_figure(env,output_dir)
    c18_model_figure(env, ln18, output_dir)
    c21_model_figure(env, ln21, output_dir)
    c24_model_figure(env, ln24, output_dir)
    model_result(env, ln18, ln21, ln24, output_dir)

if __name__=='__main__':
    main()
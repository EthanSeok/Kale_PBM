import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import os

def lai(in_square, in_circle, output_dir):
    fig1, ax1 = plt.subplots(ncols=2, sharey=True, sharex=True,figsize=(10, 5))
    colors = ["#252525", '#3182bd']
    sns.lineplot(x=in_square['leafnumber_range2'], y=in_square['LAI_expect'], color=colors[0], label='predict', ax=ax1[0], linewidth=2)
    sns.scatterplot(x=in_square['leafnumber_range2'], y=in_square['LAI'], data=lai, marker='^', color=colors[1], s=100, label='observed', ax=ax1[0])
    ax1[0].set_title('LAI Square Fit')
    ax1[0].set_ylabel('LAI ($mm^2$)')
    ax1[0].set_xlabel('Leaf Number')
    ax1[0].set(ylim=(0, 4))
    ax1[0].set(xlim=(0, 18))

    sns.lineplot(x=in_circle['leafnumber_range2'], y=in_circle['LAI_expect'], color=colors[0], label='predict', ax=ax1[1], linewidth=2)
    sns.scatterplot(x=in_circle['leafnumber_range2'], y=in_circle['LAI'], data=lai, marker='^', color=colors[1], s=100, label='observed', ax=ax1[1])
    ax1[1].set_title('LAI Circle Fit')
    ax1[1].set_ylabel('LAI ($mm^2$)')
    ax1[1].set_xlabel('Leaf Number')
    ax1[1].set(ylim=(0, 4))
    ax1[1].set(xlim=(0, 18))
    ax1[1].get_legend().remove()
    fig1.tight_layout()
    fig1.savefig(fname=f'{output_dir}/LAI_results.png', bbox_inches='tight', pad_inches=0.2)



def main():
    circle = 'kale_lai_circle.csv'
    square = 'kale_lai_square.csv'
    kale_env = '../leaf_number_increase/kale_env.csv'
    output_dir = '../output/lai/통합'

    in_circle = pd.read_csv(circle)
    in_square = pd.read_csv(square)
    env = pd.read_csv(kale_env)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    lai(in_square, in_circle, output_dir)

if __name__=='__main__':
    main()
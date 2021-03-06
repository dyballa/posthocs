__version__ = '0.2.9'

from posthocs._posthocs \
    import posthoc_conover, posthoc_dunn, posthoc_nemenyi, posthoc_ttest, posthoc_tukey_hsd, posthoc_mannwhitney

from posthocs._plotting \
    import sign_array, sign_plot, sign_table

from posthocs._outliers \
    import outliers_iqr, outliers_grubbs, outliers_tietjen, outliers_gesd

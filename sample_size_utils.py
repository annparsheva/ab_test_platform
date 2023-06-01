import scipy.stats as stats


def sample_size_calculate(significance_level, statistical_power, mde, sd):
    statistical_power = statistical_power / 100
    sample_size = (
        (stats.norm.ppf(1 - significance_level / 2) + stats.norm.ppf(statistical_power))
        ** 2
        * (sd**2 + sd**2)
    ) / mde**2
    return round(sample_size)

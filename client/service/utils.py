def print_statistics(title, mean, std, median):
    print(f'\n{title}')
    print(f'mean: {mean:.3f} ms')
    print(f'std: {std:.3f} ms;  {std*100/mean:.1f} %')
    print(f'median: {median:.3f} ms')
    print('')

    
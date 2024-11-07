def print_statistics(tree_name, mean, std, median):
    print(f'{tree_name}')
    print(f'mean: {mean:.3f} ms')
    print(f'std: {std:.3f} ms;  {std*100/mean:.1f} %')
    print(f'median: {median:.3f} ms')
    print('')

    
from utils import analysis, visualization

def main():
    orders = analysis.load_data("orders.csv")
    analysis.explore_data(orders)


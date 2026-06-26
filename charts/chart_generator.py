import matplotlib.pyplot as plt
import os


def create_charts():

    os.makedirs("charts/output", exist_ok=True)

    # -----------------------
    # Bar Chart
    # -----------------------

    categories = [
        "Research",
        "Planning",
        "Writing",
        "PDF",
        "PPT"
    ]

    values = [95, 90, 88, 85, 80]

    plt.figure(figsize=(6, 4))
    plt.bar(categories, values)
    plt.title("Agent Performance")
    plt.savefig(
        "charts/output/bar_chart.png"
    )
    plt.close()

    # -----------------------
    # Pie Chart
    # -----------------------

    plt.figure(figsize=(5, 5))

    plt.pie(
        [30, 25, 20, 15, 10],
        labels=[
            "Research",
            "Writing",
            "Planning",
            "PDF",
            "PPT"
        ],
        autopct="%1.1f%%"
    )

    plt.title("Work Distribution")

    plt.savefig(
        "charts/output/pie_chart.png"
    )

    plt.close()

    # -----------------------
    # Trend Chart
    # -----------------------

    plt.figure(figsize=(6, 4))

    plt.plot(
        [1, 2, 3, 4, 5],
        [20, 40, 55, 70, 95],
        marker="o"
    )

    plt.title("Research Progress")

    plt.xlabel("Stage")
    plt.ylabel("Completion %")

    plt.savefig(
        "charts/output/trend_chart.png"
    )

    plt.close()

    return [
        "charts/output/bar_chart.png",
        "charts/output/pie_chart.png",
        "charts/output/trend_chart.png"
    ]
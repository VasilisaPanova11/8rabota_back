from io import BytesIO
import matplotlib
import matplotlib.pyplot as plt
from django.core.files import File
from django.db.models import Sum, F, Window
from .models import Sell, Chart
from .factories import SellFactory

matplotlib.use("agg")


def get_chart():
    fig, ax = plt.subplots(figsize=(16, 9))

    fig.text(
        0.1,
        0.5,
        "ИКБО-03-22 Панова Василиса Александровна",
        fontsize=30,
        color="black",
    )
    return fig, ax


def set_settings(ax):
    ax.grid(visible=True, color="grey", linestyle="-.", linewidth=0.5, alpha=0.2)


def generate_line_chart(values, labels):
    fig, ax = get_chart()
    set_settings(ax)
    ax.plot(labels, values, marker="o", linestyle="-")
    ax.set_xticks(labels)

    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    return buffer


def generate_bar_chart(values, labels):
    fig, ax = get_chart()
    set_settings(ax)
    ax.barh(labels, values)

    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    return buffer


def generate_pie_chart(values, labels):
    fig, ax = get_chart()
    ax.pie(values, labels=labels, startangle=45)

    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    return buffer


def generate_charts():
    data = (
        Sell.objects.annotate(
            sum=Window(
                expression=Sum("count"),
                partition_by=F("mat__pk"),
            )
        )
        .distinct()
        .values("sum", "mat__title")
    )
    print(data)
    if not data.exists():
        SellFactory.create_batch(50)
    values = [item["sum"] for item in data]
    labels = [item["mat__title"] for item in data]
    charts = {
        "line": generate_line_chart(values, labels),
        "bar": generate_bar_chart(values, labels),
        "pie": generate_pie_chart(values, labels),
    }
    results = []
    for name, chart in charts.items():
        obj = Chart.objects.create(
            image=File(chart, name=name + ".png"),
        )
        results.append(obj)
    return results

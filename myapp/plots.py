from pandas import DataFrame
import matplotlib.pyplot as plt
from shared import ds_20C


def mapping(df: DataFrame):
    map = (map code goes here)
    return map


def verticle_profile(df: DataFrame, true_col: str, pred_col: str):
    fpr, tpr, _ = roc_curve(df[true_col], df[pred_col])
    roc_auc = auc(fpr, tpr)

    roc_df = DataFrame({"fpr": fpr, "tpr": tpr})

    plot = (
        ggplot(roc_df, aes(x="fpr", y="tpr"))
        + geom_line(color="darkorange", size=1.5, show_legend=True, linetype="solid")
        + geom_abline(intercept=0, slope=1, color="navy", linetype="dashed")
        + labs(
            title="Receiver Operating Characteristic (ROC)",
            subtitle=f"AUC: {roc_auc.round(2)}",
            x="False Positive Rate",
            y="True Positive Rate",
        )
        + theme_minimal()
    )

    return plot


def time_series(df: DataFrame, true_col: str, pred_col: str):
    test_2 = ds_20C.sel(time=slice("1920", "2000"))

    #select the TEMP column and set z_t, which is depth to 0 for sea surface temeperature
    test_2000_2 = test_2.TEMP.sel(z_t = 0, method = "nearest")

    #select a member_id
    point_2 = test_2000_2.sel(member_id = 2)

    #select just one point on the graph (this point is closest to channel islands)
    point_3 = point_2.isel(nlat=(280), nlon=(240))

    plot = (

        #plot out time series graph
        point_3.plot()

        #add title to graph
        plt.title("Sea Surface temperature Time Series")
    )

    return plot

    # precision, recall, _ = precision_recall_curve(df[true_col], df[pred_col])

    # pr_df = DataFrame({"precision": precision, "recall": recall})

    # plot = (
    #     ggplot(pr_df, aes(x="recall", y="precision"))
    #     + geom_line(color="darkorange", size=1.5, show_legend=True, linetype="solid")
    #     + labs(
    #         title="Precision-Recall Curve",
    #         x="Recall",
    #         y="Precision",
    #     )
    #     + theme_minimal()
    # )

    # return plot

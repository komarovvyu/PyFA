from PIL import Image
import numpy as np
import plotly.graph_objects as go
import fabio

pts_diffr_arc1 = ((228,388), (347,560), (567,740), (783,844), (1012,877), (1319,819), (1578,680), (1814,384))
pts_diffr_arc2 = ((639,75), (665,178), (784,337), (970,425), (1163,402), (1314,282), (1412,83))

#x = Image.open(r"frm/14_LaB6-LPS_150mm28deg_40_06.0001")
#x.show()
# frm_int = np.array(x.getdata()).reshape(2048,2048)
# print(frm_int.shape, np.max(frm_int), np.min(frm_int))

frm_filename = r"frm/14_LaB6-LPS_150mm28deg_40_06.0001"
frm = fabio.open(frm_filename)
frm.data = np.flip(frm.data, axis=0)
# frm.data = frm.data.astype(dtype=np.float64)
# frm.data[frm.data==0.] = np.nan
#frm_intensities = frm.data
#print("\n".join(f"{k}: {frm.header[k]}" for k in frm.header.keys()))
FRM_RANGE = ([0, frm.header['nColumns']-1], [0, frm.header['nRows']-1])
print(f"Intensities min/max = {np.min(frm.data)}/{np.max(frm.data)}")


fig_layout = dict(
    xaxis=dict(range=FRM_RANGE[0],
               showgrid=False),
    yaxis=dict(range=FRM_RANGE[1],
               showgrid=False,
               scaleanchor='x'),
    # images=dict(
    #     source=x,
    #     xref="paper",
    #     yref="paper",
    #     x=0,
    #     y=1,
    #     xanchor="left",
    #     yanchor="top",
    #     layer="below",
    #     sizing="stretch",
    #     sizex=1.0,
    #     sizey=1.0
    #          )
                 )

#print(points)
p_x = list(p[0] for p in pts_diffr_arc1)
p_y = list(p[1] for p in pts_diffr_arc1)
#print(p_x, '\n', p_y)
diffr_arc1 = go.Scatter(
    x=p_x, y=p_y,
    mode="lines",
    line=dict(color="green", width=2),
    name='Arc 1 poly'
)
p_x = list(p[0] for p in pts_diffr_arc2)
p_y = list(p[1] for p in pts_diffr_arc2)
#print(p_x, '\n', p_y)
diffr_arc2 = go.Scatter(
    x=p_x, y=p_y,
    mode="lines",
    line=dict(color="green", width=2),
    name='Arc 2 poly'
)


# x_heatmap = np.linspace(0, 1, 20)
# y_heatmap = np.linspace(0, 1, 20)
# z_heatmap = np.random.rand(20, 20)  # Матрица значений для heatmap

frm_data = go.Heatmap(
    # x=np.linspace(0, frm.header['nColumns'], frm.header['nColumns']),
    # y=np.linspace(0, frm.header['nRows'], frm.header['nColumns']),
    x0 = 0, y0 = 0,
    dx = 1, dy = 1,
    z=np.log(frm.data),
    # colorscale='Viridis',
    colorscale=[[0, 'rgb(255,255,255)'],
                [0.0001, 'rgb(200,0,0)'],
                [0.25, 'rgb(200,200,0)'],
                [0.50, 'rgb(255,255,128)'],
                [0.75, 'rgb(255,128,255)'],
                [0.9999, 'rgb(200,0,200)'],
                [1, 'rgb(0,255,0)']],
    name='Frame data'
)

fig = go.Figure(layout=fig_layout)
fig.add_trace(diffr_arc1)
fig.add_trace(diffr_arc2)
fig.add_trace(frm_data)
# fig = go.Figure(data=fig_data, layout=fig_layout)
#
#
# fig.add_layout_image(dict(
#     source=x,
#     xref="paper",
#     yref="paper",
#     x=0,
#     y=1,
#     xanchor="left",
#     yanchor="top",
#     layer="below",
#     sizing="stretch",
#     sizex=1.0,
#     sizey=1.0
# ))

fig.show()


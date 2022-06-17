import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from collections import Counter

from dfs import clean_df, make_csbm_df_function,make_sms_df,make_dact_df_function

def make_csbm_bsc_fig_function(csbm_df=make_csbm_df_function()[0]):

  # GET MAX NUMBER OF DAYS
  csbm_max_days = csbm_df['time'].max()

  # CONVERT STOOL COLUMN TO STR FOR DISCRETE COLOURS
  csbm_df['bristol_stool_chart'] = csbm_df['bristol_stool_chart'].astype(str)

  # CREATE TIMESERIES CHART
  csbm_bsc_fig = px.scatter(csbm_df, 
                        x='time',
                        y='csbm',
                        color='bristol_stool_chart',
                        opacity=0.6,
                        color_discrete_sequence=["red", "red", "orange", "green", "green","orange","red"],
                        labels=dict(time="Days since starting treatment", csbm="Complete Spontaneous Bowel Movements", bristol_stool_chart="Stool Type"), # CUSTOMISE AXIS TITLES
                        hover_name="QIPID", hover_data=["csbm", "bristol_stool_chart"], # CUSTOMISE HOVER LABELS,
                        trendline="ols", #ADD TREND LINE
                        trendline_scope = "overall",
                        
                        # SET ORDER OF LEGEND ITEMS 
                        category_orders={
                            'bristol_stool_chart' : ['1','2','3','4','5','6','7']
                        }
                        
  )

  # Set custom y-axis labels according to CSBM
  csbm_y_labs = ['< 1/week',
                'Every 7 days',
                'Every 6 days',
                'Every 5 days',
                'Every 4 days',
                'Every 3 days',
                'Every 2 days',
                'Every day',
                '>1/day']

  csbm_bsc_fig.update_yaxes(
      ticktext=csbm_y_labs,
      tickvals=list(range(1,1+len(csbm_y_labs))),
      showgrid=False
  )
  # CUSTOMISE MARKER AESTHETICS
  csbm_bsc_fig.update_traces(marker=dict(size=12,
                                line=dict(width=2,
                                          color='DarkSlateGrey')),
                    selector=dict(mode='markers')
                  )

  #CUSTOMISE DATE x AXIS FORMAT
  csbm_bsc_fig.update_xaxes(
      dtick="28",
      range=[-5,csbm_max_days+5],
      #showgrid=False
      )

  csbm_bsc_fig.update_layout(
            # title={
            #     'text': '💩 Complete Spontaneous Bowel Movements & Bristol Stool Score',
            #     'y':0.95,
            #     'x':0.5,
            #     'xanchor': 'center',
            #     'yanchor': 'top'},
              
            yaxis_title=None, #REMOVE Y TITLE

            # FIX FIGURE MARGINS
            # width=500,
            # height=500,
            margin=dict(
                l=2,
                r=2,
                b=0,
                t=0,
                pad=0
            ),
            #paper_bgcolor="LightSteelBlue",
          
          )


  # COLOUR BACKGROUND ACCORDINGLY
  csbm_bsc_fig.add_hrect(y0=10, y1=7.5, line_width=0, fillcolor="green", opacity=0.2,layer="below")
  csbm_bsc_fig.add_hrect(y0=7.5, y1=3.5, line_width=0, fillcolor="orange", opacity=0.2,layer="below")
  csbm_bsc_fig.add_hrect(y0=3.5, y1=0, line_width=0, fillcolor="red", opacity=0.2,layer="below")

  # UPDATE LEGEND POSITION

  csbm_bsc_fig.update_layout(
      
      legend=dict(
                  yanchor="top",
                  y=-0.12,
                  xanchor="center",
                  x=0.4,
                  orientation='h',
                  #bgcolor="LightSteelBlue",
                  bordercolor="Black",
                  borderwidth=1
                 )
      )



  return csbm_bsc_fig

def make_sms_fig(sms_df=make_sms_df()[0]):

  # CREATE TIMESERIES CHART
  sms_df_fig = px.scatter(sms_df, 
                            x='time',
                            y='total_score',
                            color='score_colour',
                            opacity = 0.5,
                        
                            labels=dict(time="Days since starting treatment", total_score="Total St Mark's Score", score_colour="Progress"), # CUSTOMISE AXIS TITLES
                              
                            color_discrete_map={
                              'red': "red",
                              "amber": "orange",
                              "green": "green",
                                    },

                            hover_name="QIPID", hover_data=["total_score", "score_colour"], # CUSTOMISE HOVER LABELS,
                            trendline="lowess", #ADD TREND LINE
                            trendline_scope="overall"
  )

  # ADD TITLE
  sms_df_fig.update_layout(
      
      # title={
      #     'text': "💩 St Mark's Score",
      #     'y':0.95,
      #     'x':0.5,
      #     'xanchor': 'center',
      #     'yanchor': 'top'
      #     },

      yaxis_title=None, #REMOVE Y TITLE

      # FIX FIGURE MARGINS
      # width=500,
      # height=500,
      margin=dict(
          l=0,
          r=0,
          b=0,
          t=2,
          pad=0
      ),
      #paper_bgcolor="LightSteelBlue",

      # CUSTOMISE LEGEND
      legend=dict(
            yanchor="top",
            y=-0.12,
            xanchor="center",
            x=0.5,
            orientation='h',
            #bgcolor="LightSteelBlue",
            bordercolor="Black",
            borderwidth=1
            )
          
          )

  # CUSTOMISE MARKER AESTHETICS
  sms_df_fig.update_traces(marker=dict(size=12,
                                line=dict(width=2,
                                          color='DarkSlateGrey')),
                    selector=dict(mode='markers')
                  )

  #CUSTOMISE DATE x AXIS FORMAT
  sms_df_fig.update_xaxes(
      dtick="28",
      )
  
  # COLOUR BACKGROUND ACCORDINGLY
  sms_df_fig.add_hrect(y0=-5, y1=2.6, line_width=0, fillcolor="green", opacity=0.2,layer="below")
  sms_df_fig.add_hrect(y0=2.6, y1=5.2, line_width=0, fillcolor="orange", opacity=0.2,layer="below")
  sms_df_fig.add_hrect(y0=5.2, y1=13, line_width=0, fillcolor="red", opacity=0.2,layer="below")

  # REMOVE GRIDLINES Y AXIS
  sms_df_fig.update_yaxes(
      showgrid=False,
      range=[-1,sms_df.total_score.max()+1]
  )

  return sms_df_fig

def make_dact_fig(dact_df=make_dact_df_function()[0]):

  # CREATE TIMESERIES CHART
  dact_df_fig = px.scatter(dact_df, 
                            x='time',
                            y='total_score_daily_routine',
                            color='colour',
                            opacity = 0.5,
                        
                            labels=dict(time="Days since starting treatment", colour="Progress"), # CUSTOMISE AXIS TITLES
                              
                            color_discrete_map={
                              'red': "red",
                              "amber": "orange",
                              "green": "green",
                                    },

                            hover_name="QIPID", hover_data=["total_score_daily_routine", "colour"], # CUSTOMISE HOVER LABELS,
                            trendline="lowess", #ADD TREND LINE
                            trendline_scope="overall"
  )

  # ADD TITLE
  dact_df_fig.update_layout(
      
      # title={
      #     'text': "💩 St Mark's Score",
      #     'y':0.95,
      #     'x':0.5,
      #     'xanchor': 'center',
      #     'yanchor': 'top'
      #     },

      yaxis_title=None, #REMOVE Y TITLE

      # FIX FIGURE MARGINS
      # width=500,
      # height=500,
      margin=dict(
          l=0,
          r=0,
          b=0,
          t=2,
          pad=0
      ),
      #paper_bgcolor="LightSteelBlue",

      # CUSTOMISE LEGEND
      legend=dict(
            yanchor="top",
            y=-0.12,
            xanchor="center",
            x=0.5,
            orientation='h',
            #bgcolor="LightSteelBlue",
            bordercolor="Black",
            borderwidth=1
            )
          
          )

  # CUSTOMISE MARKER AESTHETICS
  dact_df_fig.update_traces(marker=dict(size=12,
                                line=dict(width=2,
                                          color='DarkSlateGrey')),
                    selector=dict(mode='markers')
                  )

  #CUSTOMISE DATE x AXIS FORMAT
  dact_df_fig.update_xaxes(
      dtick="28",
      )
  
  # COLOUR BACKGROUND ACCORDINGLY
  dact_df_fig.add_hrect(y0=45, y1=39, line_width=0, fillcolor="green", opacity=0.2,layer="below")
  dact_df_fig.add_hrect(y0=39, y1=34.5, line_width=0, fillcolor="orange", opacity=0.2,layer="below")
  dact_df_fig.add_hrect(y0=34.5, y1=-1, line_width=0, fillcolor="red", opacity=0.2,layer="below")

  # REMOVE GRIDLINES Y AXIS
  dact_df_fig.update_yaxes(
      showgrid=False,
      range=[-1,45]
  )

  return dact_df_fig


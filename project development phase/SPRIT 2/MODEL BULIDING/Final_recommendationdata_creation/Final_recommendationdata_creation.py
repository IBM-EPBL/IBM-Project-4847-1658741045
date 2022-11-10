{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Creating final data for crop and fertilizer recommendation system"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "fertilizer_data_path = '../Data-raw/FertilizerData.csv'\n",
    "merge_fert = pd.read_csv(fertilizer_data_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Crop</th>\n",
       "      <th>N</th>\n",
       "      <th>P</th>\n",
       "      <th>K</th>\n",
       "      <th>pH</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>rice</td>\n",
       "      <td>80</td>\n",
       "      <td>40</td>\n",
       "      <td>40</td>\n",
       "      <td>5.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>maize</td>\n",
       "      <td>80</td>\n",
       "      <td>40</td>\n",
       "      <td>20</td>\n",
       "      <td>5.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>chickpea</td>\n",
       "      <td>40</td>\n",
       "      <td>60</td>\n",
       "      <td>80</td>\n",
       "      <td>5.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>12</td>\n",
       "      <td>kidneybeans</td>\n",
       "      <td>20</td>\n",
       "      <td>60</td>\n",
       "      <td>20</td>\n",
       "      <td>5.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>13</td>\n",
       "      <td>pigeonpeas</td>\n",
       "      <td>20</td>\n",
       "      <td>60</td>\n",
       "      <td>20</td>\n",
       "      <td>5.5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0         Crop   N   P   K   pH\n",
       "0           0         rice  80  40  40  5.5\n",
       "1           3        maize  80  40  20  5.5\n",
       "2           5     chickpea  40  60  80  5.5\n",
       "3          12  kidneybeans  20  60  20  5.5\n",
       "4          13   pigeonpeas  20  60  20  5.5"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merge_fert.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "del merge_fert['Unnamed: 0']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>N</th>\n",
       "      <th>P</th>\n",
       "      <th>K</th>\n",
       "      <th>pH</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>22.000000</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>22.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>50.454545</td>\n",
       "      <td>45.681818</td>\n",
       "      <td>48.181818</td>\n",
       "      <td>5.409091</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>36.315715</td>\n",
       "      <td>32.634172</td>\n",
       "      <td>51.698426</td>\n",
       "      <td>0.590326</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>20.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>4.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>5.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>30.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>5.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>80.000000</td>\n",
       "      <td>60.000000</td>\n",
       "      <td>50.000000</td>\n",
       "      <td>5.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>120.000000</td>\n",
       "      <td>125.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>6.500000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                N           P           K         pH\n",
       "count   22.000000   22.000000   22.000000  22.000000\n",
       "mean    50.454545   45.681818   48.181818   5.409091\n",
       "std     36.315715   32.634172   51.698426   0.590326\n",
       "min     20.000000   10.000000   10.000000   4.000000\n",
       "25%     20.000000   20.000000   20.000000   5.500000\n",
       "50%     30.000000   40.000000   30.000000   5.500000\n",
       "75%     80.000000   60.000000   50.000000   5.500000\n",
       "max    120.000000  125.000000  200.000000   6.500000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merge_fert.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',\n",
       "       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',\n",
       "       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',\n",
       "       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merge_fert['Crop'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x294c8c8bfa0>]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(merge_fert[\"N\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x294cad60550>]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(merge_fert[\"P\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x294cadb7b50>]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(merge_fert[\"K\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(merge_fert.corr(),annot=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "merge_crop = pd.read_csv('../Data-raw/MergeFileCrop.csv')\n",
    "reco_fert = merge_fert"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Add +/-3 for every NPK value\n",
    "import random\n",
    "temp = pd.DataFrame(columns = ['N','P','K'])\n",
    "for i in range(0,merge_crop.shape[0]):\n",
    "    crop = merge_crop.label.iloc[i]\n",
    "    #print(crop)\n",
    "    N = reco_fert[reco_fert['Crop'] == crop][\"N\"].iloc[0] + random.randint(-20,20)\n",
    "    P = reco_fert[reco_fert['Crop'] == crop][\"P\"].iloc[0] + random.randint(-5,20)\n",
    "    K = reco_fert[reco_fert['Crop'] == crop][\"K\"].iloc[0] + random.randint(-5,5)\n",
    "    d = {\"N\":N,\"P\":P,\"K\":K}\n",
    "    #print(d)\n",
    "    temp = temp.append(d,ignore_index = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>N</th>\n",
       "      <th>P</th>\n",
       "      <th>K</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>90</td>\n",
       "      <td>42</td>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>85</td>\n",
       "      <td>58</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>60</td>\n",
       "      <td>55</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>74</td>\n",
       "      <td>35</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>78</td>\n",
       "      <td>42</td>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2195</th>\n",
       "      <td>107</td>\n",
       "      <td>34</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2196</th>\n",
       "      <td>99</td>\n",
       "      <td>15</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2197</th>\n",
       "      <td>118</td>\n",
       "      <td>33</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2198</th>\n",
       "      <td>117</td>\n",
       "      <td>32</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2199</th>\n",
       "      <td>104</td>\n",
       "      <td>18</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2200 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        N   P   K\n",
       "0      90  42  43\n",
       "1      85  58  41\n",
       "2      60  55  44\n",
       "3      74  35  40\n",
       "4      78  42  42\n",
       "...   ...  ..  ..\n",
       "2195  107  34  32\n",
       "2196   99  15  27\n",
       "2197  118  33  30\n",
       "2198  117  32  34\n",
       "2199  104  18  30\n",
       "\n",
       "[2200 rows x 3 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "merge_crop['N'] = temp['N']\n",
    "merge_crop['P'] = temp['P']\n",
    "merge_crop['K'] = temp['K']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>temperature</th>\n",
       "      <th>humidity</th>\n",
       "      <th>ph</th>\n",
       "      <th>rainfall</th>\n",
       "      <th>label</th>\n",
       "      <th>N</th>\n",
       "      <th>P</th>\n",
       "      <th>K</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>20.879744</td>\n",
       "      <td>82.002744</td>\n",
       "      <td>6.502985</td>\n",
       "      <td>202.935536</td>\n",
       "      <td>rice</td>\n",
       "      <td>90</td>\n",
       "      <td>42</td>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>21.770462</td>\n",
       "      <td>80.319644</td>\n",
       "      <td>7.038096</td>\n",
       "      <td>226.655537</td>\n",
       "      <td>rice</td>\n",
       "      <td>85</td>\n",
       "      <td>58</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>23.004459</td>\n",
       "      <td>82.320763</td>\n",
       "      <td>7.840207</td>\n",
       "      <td>263.964248</td>\n",
       "      <td>rice</td>\n",
       "      <td>60</td>\n",
       "      <td>55</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>26.491096</td>\n",
       "      <td>80.158363</td>\n",
       "      <td>6.980401</td>\n",
       "      <td>242.864034</td>\n",
       "      <td>rice</td>\n",
       "      <td>74</td>\n",
       "      <td>35</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>20.130175</td>\n",
       "      <td>81.604873</td>\n",
       "      <td>7.628473</td>\n",
       "      <td>262.717340</td>\n",
       "      <td>rice</td>\n",
       "      <td>78</td>\n",
       "      <td>42</td>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2195</th>\n",
       "      <td>895</td>\n",
       "      <td>26.774637</td>\n",
       "      <td>66.413269</td>\n",
       "      <td>6.780064</td>\n",
       "      <td>177.774507</td>\n",
       "      <td>coffee</td>\n",
       "      <td>107</td>\n",
       "      <td>34</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2196</th>\n",
       "      <td>896</td>\n",
       "      <td>27.417112</td>\n",
       "      <td>56.636362</td>\n",
       "      <td>6.086922</td>\n",
       "      <td>127.924610</td>\n",
       "      <td>coffee</td>\n",
       "      <td>99</td>\n",
       "      <td>15</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2197</th>\n",
       "      <td>897</td>\n",
       "      <td>24.131797</td>\n",
       "      <td>67.225123</td>\n",
       "      <td>6.362608</td>\n",
       "      <td>173.322839</td>\n",
       "      <td>coffee</td>\n",
       "      <td>118</td>\n",
       "      <td>33</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2198</th>\n",
       "      <td>898</td>\n",
       "      <td>26.272418</td>\n",
       "      <td>52.127394</td>\n",
       "      <td>6.758793</td>\n",
       "      <td>127.175293</td>\n",
       "      <td>coffee</td>\n",
       "      <td>117</td>\n",
       "      <td>32</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2199</th>\n",
       "      <td>899</td>\n",
       "      <td>23.603016</td>\n",
       "      <td>60.396475</td>\n",
       "      <td>6.779833</td>\n",
       "      <td>140.937041</td>\n",
       "      <td>coffee</td>\n",
       "      <td>104</td>\n",
       "      <td>18</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2200 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Unnamed: 0  temperature   humidity        ph    rainfall   label    N  \\\n",
       "0              0    20.879744  82.002744  6.502985  202.935536    rice   90   \n",
       "1              1    21.770462  80.319644  7.038096  226.655537    rice   85   \n",
       "2              2    23.004459  82.320763  7.840207  263.964248    rice   60   \n",
       "3              3    26.491096  80.158363  6.980401  242.864034    rice   74   \n",
       "4              4    20.130175  81.604873  7.628473  262.717340    rice   78   \n",
       "...          ...          ...        ...       ...         ...     ...  ...   \n",
       "2195         895    26.774637  66.413269  6.780064  177.774507  coffee  107   \n",
       "2196         896    27.417112  56.636362  6.086922  127.924610  coffee   99   \n",
       "2197         897    24.131797  67.225123  6.362608  173.322839  coffee  118   \n",
       "2198         898    26.272418  52.127394  6.758793  127.175293  coffee  117   \n",
       "2199         899    23.603016  60.396475  6.779833  140.937041  coffee  104   \n",
       "\n",
       "       P   K  \n",
       "0     42  43  \n",
       "1     58  41  \n",
       "2     55  44  \n",
       "3     35  40  \n",
       "4     42  42  \n",
       "...   ..  ..  \n",
       "2195  34  32  \n",
       "2196  15  27  \n",
       "2197  33  30  \n",
       "2198  32  34  \n",
       "2199  18  30  \n",
       "\n",
       "[2200 rows x 9 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merge_crop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "del merge_crop['Unnamed: 0']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>temperature</th>\n",
       "      <th>humidity</th>\n",
       "      <th>ph</th>\n",
       "      <th>rainfall</th>\n",
       "      <th>label</th>\n",
       "      <th>N</th>\n",
       "      <th>P</th>\n",
       "      <th>K</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20.879744</td>\n",
       "      <td>82.002744</td>\n",
       "      <td>6.502985</td>\n",
       "      <td>202.935536</td>\n",
       "      <td>rice</td>\n",
       "      <td>90</td>\n",
       "      <td>42</td>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>21.770462</td>\n",
       "      <td>80.319644</td>\n",
       "      <td>7.038096</td>\n",
       "      <td>226.655537</td>\n",
       "      <td>rice</td>\n",
       "      <td>85</td>\n",
       "      <td>58</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>23.004459</td>\n",
       "      <td>82.320763</td>\n",
       "      <td>7.840207</td>\n",
       "      <td>263.964248</td>\n",
       "      <td>rice</td>\n",
       "      <td>60</td>\n",
       "      <td>55</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>26.491096</td>\n",
       "      <td>80.158363</td>\n",
       "      <td>6.980401</td>\n",
       "      <td>242.864034</td>\n",
       "      <td>rice</td>\n",
       "      <td>74</td>\n",
       "      <td>35</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>20.130175</td>\n",
       "      <td>81.604873</td>\n",
       "      <td>7.628473</td>\n",
       "      <td>262.717340</td>\n",
       "      <td>rice</td>\n",
       "      <td>78</td>\n",
       "      <td>42</td>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2195</th>\n",
       "      <td>26.774637</td>\n",
       "      <td>66.413269</td>\n",
       "      <td>6.780064</td>\n",
       "      <td>177.774507</td>\n",
       "      <td>coffee</td>\n",
       "      <td>107</td>\n",
       "      <td>34</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2196</th>\n",
       "      <td>27.417112</td>\n",
       "      <td>56.636362</td>\n",
       "      <td>6.086922</td>\n",
       "      <td>127.924610</td>\n",
       "      <td>coffee</td>\n",
       "      <td>99</td>\n",
       "      <td>15</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2197</th>\n",
       "      <td>24.131797</td>\n",
       "      <td>67.225123</td>\n",
       "      <td>6.362608</td>\n",
       "      <td>173.322839</td>\n",
       "      <td>coffee</td>\n",
       "      <td>118</td>\n",
       "      <td>33</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2198</th>\n",
       "      <td>26.272418</td>\n",
       "      <td>52.127394</td>\n",
       "      <td>6.758793</td>\n",
       "      <td>127.175293</td>\n",
       "      <td>coffee</td>\n",
       "      <td>117</td>\n",
       "      <td>32</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2199</th>\n",
       "      <td>23.603016</td>\n",
       "      <td>60.396475</td>\n",
       "      <td>6.779833</td>\n",
       "      <td>140.937041</td>\n",
       "      <td>coffee</td>\n",
       "      <td>104</td>\n",
       "      <td>18</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2200 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      temperature   humidity        ph    rainfall   label    N   P   K\n",
       "0       20.879744  82.002744  6.502985  202.935536    rice   90  42  43\n",
       "1       21.770462  80.319644  7.038096  226.655537    rice   85  58  41\n",
       "2       23.004459  82.320763  7.840207  263.964248    rice   60  55  44\n",
       "3       26.491096  80.158363  6.980401  242.864034    rice   74  35  40\n",
       "4       20.130175  81.604873  7.628473  262.717340    rice   78  42  42\n",
       "...           ...        ...       ...         ...     ...  ...  ..  ..\n",
       "2195    26.774637  66.413269  6.780064  177.774507  coffee  107  34  32\n",
       "2196    27.417112  56.636362  6.086922  127.924610  coffee   99  15  27\n",
       "2197    24.131797  67.225123  6.362608  173.322839  coffee  118  33  30\n",
       "2198    26.272418  52.127394  6.758793  127.175293  coffee  117  32  34\n",
       "2199    23.603016  60.396475  6.779833  140.937041  coffee  104  18  30\n",
       "\n",
       "[2200 rows x 8 columns]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merge_crop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "merge_crop = merge_crop[[ 'N', 'P', 'K','temperature', 'humidity', 'ph', 'rainfall', 'label']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "merge_crop.to_csv(\"../Data-processed/crop_recommendation.csv\",index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Checking if everything went fine\n",
    "df = pd.read_csv('../Data-processed/crop_recommendation.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>N</th>\n",
       "      <th>P</th>\n",
       "      <th>K</th>\n",
       "      <th>temperature</th>\n",
       "      <th>humidity</th>\n",
       "      <th>ph</th>\n",
       "      <th>rainfall</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>90</td>\n",
       "      <td>42</td>\n",
       "      <td>43</td>\n",
       "      <td>20.879744</td>\n",
       "      <td>82.002744</td>\n",
       "      <td>6.502985</td>\n",
       "      <td>202.935536</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>85</td>\n",
       "      <td>58</td>\n",
       "      <td>41</td>\n",
       "      <td>21.770462</td>\n",
       "      <td>80.319644</td>\n",
       "      <td>7.038096</td>\n",
       "      <td>226.655537</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>60</td>\n",
       "      <td>55</td>\n",
       "      <td>44</td>\n",
       "      <td>23.004459</td>\n",
       "      <td>82.320763</td>\n",
       "      <td>7.840207</td>\n",
       "      <td>263.964248</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>74</td>\n",
       "      <td>35</td>\n",
       "      <td>40</td>\n",
       "      <td>26.491096</td>\n",
       "      <td>80.158363</td>\n",
       "      <td>6.980401</td>\n",
       "      <td>242.864034</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>78</td>\n",
       "      <td>42</td>\n",
       "      <td>42</td>\n",
       "      <td>20.130175</td>\n",
       "      <td>81.604873</td>\n",
       "      <td>7.628473</td>\n",
       "      <td>262.717340</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    N   P   K  temperature   humidity        ph    rainfall label\n",
       "0  90  42  43    20.879744  82.002744  6.502985  202.935536  rice\n",
       "1  85  58  41    21.770462  80.319644  7.038096  226.655537  rice\n",
       "2  60  55  44    23.004459  82.320763  7.840207  263.964248  rice\n",
       "3  74  35  40    26.491096  80.158363  6.980401  242.864034  rice\n",
       "4  78  42  42    20.130175  81.604873  7.628473  262.717340  rice"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2200, 8)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
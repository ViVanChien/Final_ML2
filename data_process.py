{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0e7ee8ab-78f9-488b-8f95-d1ad549fe1c8",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: '-f'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 10\u001b[0m\n\u001b[0;32m      8\u001b[0m chunksize \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m10000\u001b[39m \u001b[38;5;66;03m# set chunksize as needed\u001b[39;00m\n\u001b[0;32m      9\u001b[0m dfs \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m---> 10\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m chunk \u001b[38;5;129;01min\u001b[39;00m \u001b[43mpd\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mread_csv\u001b[49m\u001b[43m(\u001b[49m\u001b[43mFile_path\u001b[49m\u001b[43m,\u001b[49m\u001b[43msep\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;130;43;01m\\t\u001b[39;49;00m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mon_bad_lines\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mskip\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43mchunksize\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;241;43m1000\u001b[39;49m\u001b[43m)\u001b[49m:\n\u001b[0;32m     11\u001b[0m     dfs\u001b[38;5;241m.\u001b[39mappend(chunk)\n\u001b[0;32m     12\u001b[0m df \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mconcat(dfs,ignore_index\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:912\u001b[0m, in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[0m\n\u001b[0;32m    899\u001b[0m kwds_defaults \u001b[38;5;241m=\u001b[39m _refine_defaults_read(\n\u001b[0;32m    900\u001b[0m     dialect,\n\u001b[0;32m    901\u001b[0m     delimiter,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    908\u001b[0m     dtype_backend\u001b[38;5;241m=\u001b[39mdtype_backend,\n\u001b[0;32m    909\u001b[0m )\n\u001b[0;32m    910\u001b[0m kwds\u001b[38;5;241m.\u001b[39mupdate(kwds_defaults)\n\u001b[1;32m--> 912\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_read\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:577\u001b[0m, in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    574\u001b[0m _validate_names(kwds\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnames\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    576\u001b[0m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[1;32m--> 577\u001b[0m parser \u001b[38;5;241m=\u001b[39m \u001b[43mTextFileReader\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    579\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[0;32m    580\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1407\u001b[0m, in \u001b[0;36mTextFileReader.__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m   1404\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m kwds[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m   1406\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles: IOHandles \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m-> 1407\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_engine \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_make_engine\u001b[49m\u001b[43m(\u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mengine\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1661\u001b[0m, in \u001b[0;36mTextFileReader._make_engine\u001b[1;34m(self, f, engine)\u001b[0m\n\u001b[0;32m   1659\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m mode:\n\u001b[0;32m   1660\u001b[0m         mode \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1661\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;241m=\u001b[39m \u001b[43mget_handle\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   1662\u001b[0m \u001b[43m    \u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1663\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1664\u001b[0m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mencoding\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1665\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mcompression\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1666\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmemory_map\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mmemory_map\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1667\u001b[0m \u001b[43m    \u001b[49m\u001b[43mis_text\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mis_text\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1668\u001b[0m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mencoding_errors\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mstrict\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1669\u001b[0m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mstorage_options\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1670\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1671\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1672\u001b[0m f \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles\u001b[38;5;241m.\u001b[39mhandle\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\common.py:859\u001b[0m, in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    854\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m    855\u001b[0m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[0;32m    856\u001b[0m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[0;32m    857\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mencoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mmode:\n\u001b[0;32m    858\u001b[0m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[1;32m--> 859\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\n\u001b[0;32m    860\u001b[0m \u001b[43m            \u001b[49m\u001b[43mhandle\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    861\u001b[0m \u001b[43m            \u001b[49m\u001b[43mioargs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    862\u001b[0m \u001b[43m            \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mioargs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    863\u001b[0m \u001b[43m            \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    864\u001b[0m \u001b[43m            \u001b[49m\u001b[43mnewline\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[0;32m    865\u001b[0m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    866\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    867\u001b[0m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[0;32m    868\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(handle, ioargs\u001b[38;5;241m.\u001b[39mmode)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '-f'"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import sys\n",
    "\n",
    "# get the command line arguments\n",
    "args = sys.argv\n",
    "File_path = args[1]\n",
    "# read the data\n",
    "chunksize = 10000 # set chunksize as needed\n",
    "dfs = []\n",
    "for chunk in pd.read_csv(File_path,sep='\\t', on_bad_lines='skip',chunksize=1000):\n",
    "    dfs.append(chunk)\n",
    "df = pd.concat(dfs,ignore_index=True)\n",
    "new_df = df.sort_values(by = \"total_votes\", ascending = False).iloc[:200]\n",
    "new_df.drop(columns=[\"review_headline\",\"review_body\"],axis = 1, inplace = True)\n",
    "file_name = File_path.replace(\".\",\"\").replace(\"/\",\"\")\n",
    "new_df.to_csv(\"Processed_\"+file_name+\".csv\", index = False)#"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b3db97f-85c6-4d64-84d8-657581072d97",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

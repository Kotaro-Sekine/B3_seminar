{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "観察列\n",
      "['a', 't', 'g', 'c', 'g', 'c', 'g', 'c']\n",
      "<前向きアルゴリズムの結果P(x)>\n",
      "0.0002889011200000003\n",
      "<viterbiアルゴリズムの結果,argmaxP(x,π)>\n",
      "['-', '+', '+', '+', '+', '+', '+', '+']\n",
      "<viterbiアルゴリズムの結果maxP(x,π)>\n",
      "6.442450944000006e-05\n"
     ]
    }
   ],
   "source": [
    "#coding:utf-8\n",
    "import csv #csvモジュールをインポート\n",
    "with open(\"test.csv\",\"r\") as f:\n",
    "    reader=csv.reader(f)\n",
    "    for i in reader:\n",
    "        observations=i\n",
    "###上はdna配列情報をcsvで読み取る操作\n",
    "\n",
    "states=('+','-')\n",
    "\n",
    "#observations = ('a', 'g', 'c','c')#観察列を直接入力するならこれを使う\n",
    "\n",
    "start_probab = {'+': 0.5, '-': 0.5}#開始状態からの遷移確率\n",
    "\n",
    "transition_probab = {#遷移確率\n",
    "'+' : {'+': 0.8, '-': 0.2}, #+の次は+へ遷移が0.8，-が0.2\n",
    "'-' : {'+': 0.4, '-': 0.6},\n",
    "}\n",
    "\n",
    "emission_probab = {#出力確率\n",
    "'+' : {'a': 0.1, 't': 0.1, 'g': 0.4,'c':0.4},\n",
    "'-' : {'a': 0.3, 't': 0.3, 'g': 0.2,'c':0.2},\n",
    "}\n",
    "def forward_viterbi(y, X, sp, tp, ep):\n",
    "    T = {}\n",
    "    for state in X:\n",
    "        ##          prob.      V. path  V. prob.\n",
    "        T[state] = (sp[state], [state], sp[state])\n",
    "    for output in y[1:]:\n",
    "        U = {}\n",
    "        for next_state in X:\n",
    "            total = 0\n",
    "            argmax = None\n",
    "            valmax = 0\n",
    "##probは初期状態から現在の経路までの全ての経路の確率足し合わせ\n",
    "##v_pathは現在の状態までのviterbiアルゴリズムによる最も尤もらしいパス\n",
    "##v_pathは現在の経路までの最も尤もらしいパスの確率\n",
    "            for source_state in X:\n",
    "                (prob, v_path, v_prob) = T[source_state]\n",
    "                p = ep[source_state][output] * tp[source_state][next_state]\n",
    "                prob *= p\n",
    "                v_prob *= p\n",
    "                total += prob\n",
    "                if v_prob > valmax:\n",
    "                    argmax = v_path + [next_state]\n",
    "                    valmax = v_prob\n",
    "            U[next_state] = (total, argmax, valmax)\n",
    "        T = U\n",
    "        \n",
    "    ## 最後の状態において総和と最大を計算\n",
    "    total = 0\n",
    "    argmax = None\n",
    "    valmax = 0\n",
    "    for state in X:\n",
    "        (prob, v_path, v_prob) = T[state]\n",
    "        total += prob\n",
    "        if v_prob > valmax:\n",
    "            argmax = v_path\n",
    "            valmax = v_prob\n",
    "    return (total, argmax, valmax)\n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    print(\"観察列\")\n",
    "    print (observations)\n",
    "    a,b,c = forward_viterbi(observations,states,\n",
    "                          start_probab,transition_probab,emission_probab)\n",
    "    print(\"<前向きアルゴリズムの結果P(x)>\")\n",
    "    print(a)\n",
    "    print(\"<viterbiアルゴリズムの結果,argmaxP(x,π)>\")\n",
    "    print(b)\n",
    "    print(\"<viterbiアルゴリズムの結果maxP(x,π)>\")\n",
    "    print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

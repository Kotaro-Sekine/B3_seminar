from automata.pda.dpda import DPDA
    # RNAステムループ構造解析",
    # gccgaaagccなど，gaaaを間(ループ)に挟んだRNAステムループ構造の配列を入力するとaccepted,そうでなければrejectedを返す",
dpda = DPDA(
        states={'q0', 'q1', 'q2', 'q3','q4','q5'},
        input_symbols={'g','c','a','u'},
        stack_symbols={'S', '1','2','3','g','c','a','u'},
        transitions={
         'q0': {
                'g': {'S': ('q1', ('1','c'))},# gが観測されたらSをpopし,g1cをpush,さらにgをpopして次の状態へ
                'c': {'S': ('q1', ('1','g'))},
                'a': {'S': ('q1', ('1','u'))},
                'u': {'S': ('q1', ('1','a'))}
           },
            'q1': {
                'g': {'1': ('q2', ('2','c'))},
                'c': {'1': ('q2', ('2','g'))},
                'a': {'1': ('q2', ('2','u'))},
                'u': {'1': ('q2', ('2','a'))}
            },
            'q2': {
                'g': {'2': ('q3', ('3','c'))},
                'c': {'2': ('q3', ('3','g'))},
                'a': {'2': ('q3', ('3','u'))},
                'u': {'2': ('q3', ('3','a'))}
            },
           'q3': {
                'g': {'3': ('q4', ('a','a','a'))}  #gが観測されたらgaaaをpush,さらにgをpopし次の状態へ
            },
           'q4': {
                'g': {'g': ('q4',(''))},  #gをpop
                'c': {'c': ('q4',(''))},
                'a': {'a': ('q4',(''))},
                'u': {'u': ('q4',(''))},
                '': {'S': ('q5', ('S',))}  #スタックと入力が共に空になれば正常終了
            }
        },
        initial_state='q0',
        initial_stack_symbol='S',
       final_states={'q5'}
   )
  
if dpda.accepts_input('gccgaaaggc'):#ここに配列入力
        print('accepted')
else:
        print('rejected')

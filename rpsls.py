#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


     #��дִ�д���,������ɺ�passɾ��
    if name=="ʯͷ":
        number=0
        return number
    if name=="ʷ����":
        number=1
        return number
    if name=="ֽ":
        number=2
        return number
    if name=="����":
        number=3
        return number
    if name=="����":
        number=4
        return number

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

     #��дִ�д���,������ɺ�passɾ��
    if number==0:
        name=str("ʯͷ")
        return name
    if number==1:
        name=str("ʷ����")
        return name
    if number==2:
        name=str("ֽ")
        return name
    if number==3:
        name=str("����")
        return name
    if number==4:
        name=str("����")
        return name

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass
    if player_choice_number==0 and (comp_number==3 or comp_number==4):
            print("��Ӯ��")
    elif player_choice_number==1 and (comp_number==4 or comp_number==0):
            print("��Ӯ��")
    elif player_choice_number==2 and (comp_number==0 or comp_number==1):
            print("��Ӯ��")
    elif player_choice_number==3 and (comp_number==1 or comp_number==4):
            print("��Ӯ��")
    elif player_choice_number==4 and (comp_number==2 or comp_number==3):
            print("��Ӯ��")
    elif player_choice_number==0 and comp_number==0 :
            print("���ͼ��������һ����")
    elif player_choice_number==1 and comp_number==1 :
            print("���ͼ��������һ����")
    elif player_choice_number==2 and comp_number==2 :
            print("���ͼ��������һ����")
    elif player_choice_number==3 and comp_number==3 :
            print("���ͼ��������һ����")
    elif player_choice_number==4 and comp_number==4 :
            print("���ͼ��������һ����")
    elif comp_number==0 and (player_choice_number==3 or player_choice_number==4):
            print("�����Ӯ��")
    elif comp_number==1 and (player_choice_number==4 or player_choice_number==0):
            print("�����Ӯ��")
    elif comp_number==2 and (player_choice_number==0 or player_choice_number==1):
            print("�����Ӯ��")
    elif comp_number==3 and (player_choice_number==1 or player_choice_number==4):
            print("�����Ӯ��")
    elif comp_number==4 and (player_choice_number==2 or player_choice_number==3):
            print("�����Ӯ��")
    else:
        print("Error: No Correct Name")

# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
player_choice=input("����������ѡ��")
comp_number = random.randrange(0, 5)
print("�������ѡ��Ϊ��" + str(number_to_name(comp_number)))
player_choice_number=name_to_number(player_choice)
rpsls(player_choice)



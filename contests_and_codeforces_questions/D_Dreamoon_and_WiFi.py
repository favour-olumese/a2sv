a = input()
m = input()

a_pluses = a.count('+')
a_minuses = a.count('-')
m_pluses = m.count('+') 
m_minuses = m.count('-')

result = 0

if m_pluses > a_pluses:
    result += a_pluses
elif m_pluses <= a_pluses:
    result += m_pluses

if m_minuses > a_minuses:
    result += a_minuses
elif m_minuses <= a_minuses:
    result += m_minuses

result = result / len(a)
print(f'{result:.12f}')
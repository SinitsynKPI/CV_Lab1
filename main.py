from level1_2d import run_2d_variant_20
from level2_3d import run_3d_variant_20
from level3_full import run_full_variant_20


def main():
    print("=" * 60)
    print(" ЛАБОРАТОРНА РОБОТА №1: Технології Computer Vision")
    print(" Сертифікатна програма Data Science (Sigma Software)")
    print(" Виконав: студент групи ІП-43 Сініцин Володимир")
    print(" Варіант: 20")
    print("=" * 60)

    while True:
        print("\nОберіть рівень завдання для запуску:")
        print("1 - Рівень I: 2D (пентагон: масштабування -> переміщення+обертання)")
        print("2 - Рівень II: 3D (піраміда з трикутною основою)")
        print("3 - Рівень III: обидва завдання в одному вікні")
        print("0 - Вихід")
        choice = input("\nВаш вибір (0-3): ").strip()

        if choice == '1':
            print("\n[Запуск] Рівень I... Закрийте вікно для повернення в меню.")
            run_2d_variant_20()
        elif choice == '2':
            print("\n[Запуск] Рівень II... Закрийте вікно для повернення в меню.")
            run_3d_variant_20()
        elif choice == '3':
            print("\n[Запуск] Рівень III... Закрийте вікно для повернення в меню.")
            run_full_variant_20()
        elif choice == '0':
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Помилка: введіть число від 0 до 3.")


if __name__ == "__main__":
    main()
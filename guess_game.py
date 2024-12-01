import random  # Rastgele sayı üretmek için random modülünü içe aktar

# Rastgele bir sayı seç (0 ile 1000 arasında)
number = random.randint(0, 1000)

# Kullanıcıya "Adam" olup olmadığını sor
is_adam = input("Are you Adam? (Y/N): ").strip().lower()  # Girişten boşlukları sil ve küçük harfe çevir

# Tahmin sayacı ve maksimum deneme hakkı
counter = 0
max_attempts = 10

# Kullanıcı "Y" veya "y" girerse oyuna başla
if is_adam == "y":
    print("Welcome to the guessing game, Adam!")
    print("Guess a number between 0 and 1000. Type -1 to quit the game.")  # Kullanıcıya oyun talimatları ver

    # Kullanıcı doğru tahmin yapana, çıkış komutunu verene ya da hakları bitene kadar döngü
    while counter < max_attempts:
        user_input = input("Please give a number to guess: ").strip()  # Kullanıcıdan tahmin al

        # Kullanıcının geçerli bir sayı girip girmediğini kontrol et
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            guess = int(user_input)  # Giriş sayısal ise integer'a dönüştür
        else:
            print("Invalid input! Please enter a valid number.")  # Geçersiz giriş için uyarı
            continue  # Döngünün başına dön ve tekrar tahmin iste

        # Kullanıcı çıkış komutu girerse (-1)
        if guess == -1:
            print("Thank you for playing the game. Goodbye!")
            break  # Döngüden çık

        counter += 1  # Tahmin sayısını artır

        # Kullanıcının tahminini kontrol et
        if guess == number:
            print(f"Congratulations! You guessed the number {number} in {counter} attempts!")  # Doğru tahmin
            break
        elif guess < number:
            print("The number is higher than your guess!")  # Sayı daha büyükse bilgilendir
        else:
            print("The number is lower than your guess!")  # Sayı daha küçükse bilgilendir

    else:
        # Kullanıcı maksimum tahmin hakkını doldurduysa
        if counter == max_attempts:
            print(f"You've used all {max_attempts} attempts. You lost! The number was {number}.")

# Kullanıcı "Adam" değilse
else:
    print("You need to be Adam to play this game. Goodbye!")  # Oyun erişimi sınırlıysa mesaj göster
